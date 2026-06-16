import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Conexion:

    @staticmethod
    def obtener_conexion():
        return psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database="bibliotecav2",
            user="postgres",
            password="FALF0307",
            port=5432
        )