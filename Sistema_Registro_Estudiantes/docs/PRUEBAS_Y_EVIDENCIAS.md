# Pruebas y evidencias para el examen

## Prueba 1: Registro exitoso
- Matrícula: A001
- Nombre: Ana López
- Edad: 20
- Carrera: Informática
- Resultado esperado: aparece mensaje de éxito y una fila A001 en la tabla.
- Evidencia: guardar captura real como `evidencias/prueba_exitosa_1.png`.

## Prueba 2: Búsqueda exitosa
- Matrícula: A001
- Pulsar Buscar.
- Resultado esperado: la tabla muestra a Ana López.
- Evidencia: guardar captura real como `evidencias/prueba_exitosa_2.png`.

## Prueba 3: Error controlado
- Intentar registrar nuevamente la matrícula A001 con datos válidos.
- Resultado esperado: aparece `Ya existe un estudiante con esa matrícula.` y no se duplica.
- Evidencia: guardar captura real como `evidencias/prueba_error.png`.

## Pruebas adicionales
- Edad negativa: se rechaza.
- Nombre vacío: se rechaza.
- Eliminar A001: desaparece de la tabla.
- Cerrar y abrir la aplicación: los datos siguen almacenados en SQLite.

## Ejecución automática
Ejecutar `python -m unittest discover -s tests -v`. Guardar la salida real si el profesor solicita evidencia adicional.

**Nota:** Las capturas de la interfaz deben hacerse en un equipo con entorno gráfico; no se incluyen capturas simuladas como si fueran pruebas reales.
