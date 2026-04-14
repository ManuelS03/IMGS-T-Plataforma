import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.config = {
            "host": "aws-1-us-east-1.pooler.supabase.com",
            "port": "6543",
            "database": "postgres",
            "user": "postgres.rhiloyfbksfwmxibhtyf",
            "password": "Ucc2026Database",
            "sslmode": "require" 
        }

    def get_connection(self):
        return psycopg2.connect(**self.config)

    def consultar(self, sql, params=None):
        conn = self.get_connection()
        # RealDictCursor permite acceder a los datos por nombre de columna
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(sql, params)
        resultado = cur.fetchall() if cur.description else None
        conn.commit()
        cur.close()
        conn.close()
        return resultado