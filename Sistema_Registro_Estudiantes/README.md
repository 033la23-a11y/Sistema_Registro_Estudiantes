# Sistema de Registro de Estudiantes
Proyecto académico de Implementación de Software desarrollado con Python, POO, Tkinter y SQLite.

## Requisitos
- Python 3.9 o superior.
- Tkinter disponible en la instalación de Python (en algunas distribuciones Linux se instala por separado).
- No requiere librerías externas ni conexión a internet.

## Ejecución
Desde la carpeta del proyecto:
```bash
python main.py
```
En Windows, si `python` no funciona, probar `py main.py`.

## Pruebas automáticas
```bash
python -m unittest discover -s tests -v
```
Estas pruebas no requieren abrir la ventana.

## Operaciones
- Registrar: completar matrícula, nombre, edad y carrera; hacer clic en Registrar.
- Buscar: escribir matrícula y hacer clic en Buscar.
- Mostrar todos: recupera la lista completa.
- Eliminar: escribir o seleccionar matrícula y confirmar.
- Limpiar: vacía los campos del formulario.

## Diseño orientado a objetos
- `Persona`: clase base, atributos protegidos, validaciones y método de información.
- `Estudiante`: hereda de Persona y sobrescribe `mostrar_informacion()` (polimorfismo).
- `BaseDatos`: crea el esquema SQLite y administra conexiones.
- `GestorEstudiantes`: lógica de negocio y operaciones de estudiantes.
- `InterfazEstudiantes`: interfaz y coordinación con el gestor.

## Evidencias y entrega
Consultar `docs/PRUEBAS_Y_EVIDENCIAS.md`. Las capturas de pantalla reales de la interfaz deben tomarse al ejecutar el sistema en la computadora. Los nombres y commits deben corresponder a la participación real de cada integrante.
