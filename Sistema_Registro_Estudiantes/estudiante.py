from persona import Persona

class Estudiante(Persona):
    """Hereda de Persona y especializa la información del estudiante."""
    def __init__(self, matricula: str, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        matricula = matricula.strip().upper()
        carrera = carrera.strip()
        if not matricula:
            raise ValueError('La matrícula es obligatoria.')
        if not carrera:
            raise ValueError('La carrera es obligatoria.')
        self._matricula = matricula
        self._carrera = carrera

    @property
    def matricula(self):
        return self._matricula

    @property
    def carrera(self):
        return self._carrera

    def mostrar_informacion(self):
        return f'{self.matricula} - {super().mostrar_informacion()} - {self.carrera}'
