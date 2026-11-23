import tempfile
import unittest
from pathlib import Path
from base_datos import BaseDatos
from estudiante import Estudiante
from gestor_estudiantes import GestorEstudiantes
from persona import Persona

class PruebasSistema(unittest.TestCase):
    def setUp(self):
        self.directorio = tempfile.TemporaryDirectory()
        self.gestor = GestorEstudiantes(BaseDatos(Path(self.directorio.name) / 'pruebas.db'))

    def tearDown(self):
        self.directorio.cleanup()

    def test_registro_y_consulta(self):
        self.gestor.registrar(Estudiante('A001', 'Ana López', 20, 'Informática'))
        self.assertEqual(self.gestor.buscar('a001').nombre, 'Ana López')

    def test_listar(self):
        self.gestor.registrar(Estudiante('A001', 'Ana López', 20, 'Informática'))
        self.gestor.registrar(Estudiante('A002', 'Luis Pérez', 21, 'Administración'))
        self.assertEqual(len(self.gestor.listar()), 2)

    def test_eliminar(self):
        self.gestor.registrar(Estudiante('A001', 'Ana López', 20, 'Informática'))
        self.assertTrue(self.gestor.eliminar('A001'))
        self.assertIsNone(self.gestor.buscar('A001'))

    def test_duplicado(self):
        self.gestor.registrar(Estudiante('A001', 'Ana López', 20, 'Informática'))
        with self.assertRaisesRegex(ValueError, 'Ya existe'):
            self.gestor.registrar(Estudiante('A001', 'Otra persona', 21, 'Derecho'))

    def test_edad_incorrecta(self):
        with self.assertRaises(ValueError):
            Estudiante('A001', 'Ana López', -3, 'Informática')

    def test_campos_vacios(self):
        with self.assertRaises(ValueError):
            Estudiante('', 'Ana López', 20, 'Informática')

    def test_herencia_y_polimorfismo(self):
        estudiante = Estudiante('A001', 'Ana López', 20, 'Informática')
        self.assertIsInstance(estudiante, Persona)
        self.assertIn('A001', estudiante.mostrar_informacion())
        self.assertNotIn('A001', Persona('Ana López', 20).mostrar_informacion())

if __name__ == '__main__':
    unittest.main()
