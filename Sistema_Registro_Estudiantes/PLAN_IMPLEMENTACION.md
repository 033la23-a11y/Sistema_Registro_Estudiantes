# PLAN DE IMPLEMENTACIÓN
**Proyecto:** Sistema de Registro de Estudiantes  
**Asignatura:** Implementación de Software  
**Equipo:** 3 integrantes (agregar nombres antes de entregar)

## Estrategia de construcción: bottom-up
Primero se implementan las clases base `Persona` y `Estudiante`, que definen y validan los datos.  
Después se construye `GestorEstudiantes`, apoyado por `BaseDatos`, para administrar la información en SQLite.  
Finalmente se integra `InterfazEstudiantes` con Tkinter y se realizan pruebas del sistema completo.

## División de módulos
| Integrante | Módulos | Responsabilidad |
|---|---|---|
| Persona 1: [luis angel | `persona.py`, `estudiante.py` | Clases, herencia, atributos, validaciones y diseño UML |
| Persona 2: [brian roberto | `base_datos.py`, `gestor_estudiantes.py` | Base de datos, registro, búsqueda, consulta, eliminación |
| Persona 3: [yesi dabeth  | `interfaz.py`, `main.py` | Interfaz, integración, mensajes de error y pruebas |

## Fases de implementación
1. Definición del caso de uso y diagrama de clases.
2. Codificación de las clases y de la persistencia.
3. Desarrollo e integración de la interfaz gráfica.
4. Pruebas, trazabilidad y documentación.

## Caso de uso principal: Registrar estudiante
**Actor:** Usuario del sistema.  
**Precondición:** Programa abierto.  
**Flujo:** Introducir matrícula, nombre, edad y carrera → presionar Registrar → validar → guardar en SQLite → actualizar tabla y mostrar confirmación.  
**Flujo alternativo:** Si falta un campo, la edad no es válida o la matrícula está duplicada, se muestra un error sin guardar el registro.  
**Postcondición:** El estudiante válido queda almacenado para futuras consultas.

## Control de versiones
Cada integrante debe realizar al menos un commit propio en GitHub. Ejemplos: `feat: modelo estudiante`, `feat: gestor sqlite`, `feat: interfaz tkinter`. No presentar commits ficticios.
