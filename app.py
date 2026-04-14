from flask import Flask, render_template, request, jsonify
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
    return render_template('index.html', dimensiones=dims, preguntas=pregs, resultado=None)

@app.route('/evaluar', methods=['POST'])
def evaluar():
    nombre_empresa = request.form.get('nombre_empresa')
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("INSERT INTO empresas (nombre_empresa) VALUES (%s) RETURNING id", (nombre_empresa,))
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

        # Cálculo de puntajes normalizados
        labels, scores = [], []
        for d_id, data in puntos_dim.items():
            score = (data['suma'] / data['max'] * 5) if data['max'] > 0 else 0
            labels.append(data['nombre'])
            scores.append(round(score, 2))

        global_score = round(sum(scores) / 5, 2)
        
        # ACTUALIZACIÓN: Guardamos el puntaje final para que el chatbot lo use
        cur.execute("UPDATE empresas SET resultado_total = %s WHERE id = %s", (global_score, empresa_id))

        # GUARDADO FINAL
        conn.commit()

        # Clasificación
        if global_score <= 1: nivel = "Nivel 1: Reactivo"
        elif global_score <= 2: nivel = "Nivel 2: Inicial"
        elif global_score <= 3: nivel = "Nivel 3: Estructurado"
        elif global_score <= 4: nivel = "Nivel 4: Integrado"
        else: nivel = "Nivel 5: Estratégico"

        resultado = {
            'empresa_id': empresa_id,
            'empresa': nombre_empresa, 
            'score': global_score, 
            'nivel': nivel, 
            'labels': labels, 
            'scores': scores
        }

    except Exception as e:
        conn.rollback()
        return f"Error al guardar: {e}"
    finally:
        cur.close()
        conn.close()

    return render_template('index.html', resultado=resultado)

# Ruta para comentarios (Asegúrate de tenerla si ya la implementaste en el JS)
@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    data = request.get_json()
    empresa_id = data.get('empresa_id')
    comentario = data.get('comentario')
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE empresas SET comentario_general = %s WHERE id = %s", (comentario, empresa_id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)