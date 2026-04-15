from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "sslmode": os.getenv("DB_SSLMODE")
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, nombre FROM dimensiones ORDER BY id")
    dims = cur.fetchall()
    cur.execute("SELECT id, dimension_id, enunciado FROM preguntas ORDER BY dimension_id, id")
    pregs = cur.fetchall()
    cur.close()
    conn.close()
    # Obtenemos resultado de los argumentos de la URL si venimos de una redirección
    resultado = request.args.get('resultado') 
    return render_template('index.html', dimensiones=dims, preguntas=pregs, resultado=None)

@app.route('/evaluar', methods=['POST'])
def evaluar():
    nombre_empresa = request.form.get('nombre_empresa')
    nit = request.form.get('nit')
    ciudad = request.form.get('ciudad')
    tamano = request.form.get('tamano')

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        # 1. Insertar Empresa (Asegúrate que las columnas nit, ciudad, tamano existan en la DB)
        cur.execute("""
            INSERT INTO empresas (nombre_empresa, nit, ciudad, tamano) 
            VALUES (%s, %s, %s, %s) RETURNING id
        """, (nombre_empresa, nit, ciudad, tamano))
        
        empresa_id = cur.fetchone()['id']

        cur.execute("SELECT id, nombre FROM dimensiones ORDER BY id")
        dims = cur.fetchall()
        cur.execute("SELECT id, dimension_id FROM preguntas")
        pregs = cur.fetchall()

        puntos_dim = {d['id']: {'suma': 0, 'max': 0, 'nombre': d['nombre']} for d in dims}

        for p in pregs:
            valor = request.form.get(f"p_{p['id']}")
            if valor is not None:
                valor_int = int(valor)
                cur.execute("INSERT INTO respuestas (empresa_id, pregunta_id, valor_puntos) VALUES (%s, %s, %s)",
                            (empresa_id, p['id'], valor_int))
                
                puntos_dim[p['dimension_id']]['suma'] += valor_int
                puntos_dim[p['dimension_id']]['max'] += 4

        def obtener_nivel_texto(p):
            if p <= 1.0: return "Nivel 1: Reactivo"
            if p <= 2.0: return "Nivel 2: Inicial"
            if p <= 3.0: return "Nivel 3: Estructurado"
            if p <= 4.0: return "Nivel 4: Integrado"
            return "Nivel 5: Estratégico"

        labels, scores = [], []
        for d_id, data in puntos_dim.items():
            promedio_norm = round((data['suma'] / data['max'] * 5), 2) if data['max'] > 0 else 0
            nivel_dim = obtener_nivel_texto(promedio_norm)
            
            cur.execute("""
                INSERT INTO resultados_dimensiones (empresa_id, dimension_id, promedio, nivel_madurez)
                VALUES (%s, %s, %s, %s)
            """, (empresa_id, d_id, promedio_norm, nivel_dim))

            labels.append(data['nombre'])
            scores.append(promedio_norm)

        global_score = round(sum(scores) / len(scores), 2) if scores else 0
        cur.execute("UPDATE empresas SET resultado_total = %s WHERE id = %s", (global_score, empresa_id))

        # ¡MUY IMPORTANTE!
        conn.commit() 

        nivel_global = obtener_nivel_texto(global_score)
        resultado = {
            'empresa_id': empresa_id,
            'empresa': nombre_empresa, 
            'score': global_score, 
            'nivel': nivel_global, 
            'labels': labels, 
            'scores': scores
        }
        
        # En lugar de solo renderizar, lo ideal es pasar el objeto resultado
        return render_template('index.html', resultado=resultado)

    except Exception as e:
        if conn: conn.rollback()
        print(f"Error detectado: {e}") # Esto aparecerá en tu terminal
        return f"Error al guardar: {e}", 500
    finally:
        if cur: cur.close()
        if conn: conn.close()

@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    data = request.get_json()
    empresa_id = data.get('empresa_id')
    comentario = data.get('comentario')
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Aseguramos que pasamos los parámetros correctamente
        cur.execute("UPDATE empresas SET comentario_general = %s WHERE id = %s", (comentario, empresa_id))
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        if conn: conn.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
