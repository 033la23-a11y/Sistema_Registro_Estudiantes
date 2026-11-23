class Persona:
    """Clase base para personas del sistema."""
    def __init__(self, nombre: str, edad: int):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError('El nombre es obligatorio.')
        if not isinstance(edad, int) or not 1 <= edad <= 120:
            raise ValueError('La edad debe ser un número entero entre 1 y 120.')
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    def mostrar_informacion(self):
        return f'{self.nombre} ({self.edad} años)'
