import sqlite3
from base_datos import BaseDatos
from estudiante import Estudiante

class GestorEstudiantes:
    """Operaciones de alta, consulta, búsqueda y eliminación."""
    def __init__(self, base_datos=None):
        self.base_datos = base_datos or BaseDatos()

    @staticmethod
    def _convertir(fila):
        return Estudiante(fila[0], fila[1], fila[2], fila[3]) if fila else None

    def registrar(self, estudiante: Estudiante):
        if not isinstance(estudiante, Estudiante):
            raise TypeError('Se requiere un objeto Estudiante.')
        try:
            with self.base_datos.conectar() as conexion:
                conexion.execute('INSERT INTO estudiantes (matricula, nombre, edad, carrera) VALUES (?, ?, ?, ?)',
                                 (estudiante.matricula, estudiante.nombre, estudiante.edad, estudiante.carrera))
        except sqlite3.IntegrityError as error:
            raise ValueError('Ya existe un estudiante con esa matrícula.') from error
        return estudiante

    def buscar(self, matricula: str):
        matricula = matricula.strip().upper()
        if not matricula:
            raise ValueError('Escribe una matrícula para buscar.')
        with self.base_datos.conectar() as conexion:
            fila = conexion.execute('SELECT matricula, nombre, edad, carrera FROM estudiantes WHERE matricula = ?', (matricula,)).fetchone()
        return self._convertir(fila)

    def listar(self):
        with self.base_datos.conectar() as conexion:
            filas = conexion.execute('SELECT matricula, nombre, edad, carrera FROM estudiantes ORDER BY matricula').fetchall()
        return [self._convertir(fila) for fila in filas]

    def eliminar(self, matricula: str):
        matricula = matricula.strip().upper()
        if not matricula:
            raise ValueError('Escribe una matrícula para eliminar.')
        with self.base_datos.conectar() as conexion:
            cursor = conexion.execute('DELETE FROM estudiantes WHERE matricula = ?', (matricula,))
            return cursor.rowcount > 0
