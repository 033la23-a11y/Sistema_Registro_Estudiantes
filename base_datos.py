import sqlite3
from pathlib import Path

class BaseDatos:
    """Encapsula la conexión SQLite y la creación del esquema."""
    def __init__(self, ruta=None):
        self.ruta = str(ruta or (Path(__file__).resolve().parent / 'estudiantes.db'))
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.ruta)

    def crear_tabla(self):
        with self.conectar() as conexion:
            conexion.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                matricula TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL CHECK(edad BETWEEN 1 AND 120),
                carrera TEXT NOT NULL
            )''')
