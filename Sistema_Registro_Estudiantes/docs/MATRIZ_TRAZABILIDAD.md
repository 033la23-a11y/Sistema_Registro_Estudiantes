# Matriz de trazabilidad Diseño–Código
El diagrama de clases de este proyecto se elaboró como diseño nuevo; no se presenta como un diagrama realizado previamente en Unidad 4. Validar con el docente si acepta este cambio de proyecto.

| Elemento del diseño | Archivo / clase en código | Estado | Justificación técnica |
|---|---|---|---|
| Clase Persona (nombre, edad) | `persona.py` → `Persona` | Implementado | Atributos protegidos y propiedades de lectura. |
| Método mostrar_informacion() | `persona.py` → `Persona.mostrar_informacion` | Implementado | Devuelve nombre y edad. |
| Clase Estudiante (matrícula, carrera) | `estudiante.py` → `Estudiante` | Implementado | Hereda de Persona y valida datos. |
| Sobrescritura mostrar_informacion() | `estudiante.py` → `Estudiante.mostrar_informacion` | Implementado | Agrega matrícula y carrera. |
| Clase BaseDatos | `base_datos.py` → `BaseDatos` | Implementado | Crea tabla y conexiones SQLite. |
| Método registrar() | `gestor_estudiantes.py` → `GestorEstudiantes.registrar` | Implementado | Guarda registros y rechaza duplicados. |
| Método buscar() | `gestor_estudiantes.py` → `GestorEstudiantes.buscar` | Implementado | Consulta por matrícula. |
| Método listar() | `gestor_estudiantes.py` → `GestorEstudiantes.listar` | Implementado | Recupera registros ordenados. |
| Método eliminar() | `gestor_estudiantes.py` → `GestorEstudiantes.eliminar` | Implementado | Borra registro por matrícula. |
| Clase InterfazEstudiantes | `interfaz.py` → `InterfazEstudiantes` | Implementado | Gestiona formulario, tabla y botones. |
| Inicio del programa | `main.py` → `main` | Implementado | Inicia ventana y ciclo de eventos. |

**Ajustes realizados durante la implementación:** La persistencia SQLite se separó en `BaseDatos` para mejorar la organización. El control de matrícula duplicada se implementó con clave primaria en SQLite y mensaje de error en el gestor.
