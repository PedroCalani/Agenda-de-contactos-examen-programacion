# Agenda-de-contactos-examen-programacion

## Agenda de Contactos en Consola
Programa de python para gestionar una agenda desde la consola.
Tiene las funcionalidades básicas necesarias para una agenda de contactos.

## Características
- Crear nuevos contactos.
- Visualizar todos los contactos.
- Buscar contactos por nombre.
- Editar un contacto existente.
- Eliminar un contacto.
- Registrar acciones en un archivo ".log".

## Requisitos
Este proyecto necesita Python 3 y algunas librerías que no son instaladas por defecto:
* Pandas
* Colorama

## Cómo usar?
Cloná o descargá el respositorio con los archivos.

Creá tu entorno virtual e instalá los módulos necesarios. Para eso, en un terminal ejecuta:
1) Ir a la carpeta: cd ruta\a\la\carpeta
2) Crear el entorno con: python -m venv NombreDelEntornoVirtual
3) Activarlo: NombreDelEntornoVirtual\Scripts\activate
4) instalar los módulos: pip install -r requirements.txt
Por último, cuando quieras desactivar el entorno virtual: deactivate

Ejecutá agenda.py

El manejo de la agenda es realizado completamente mediante inputs, generalmente con valores numéricos.

## Estructura del proyecto
* agenda.py                   # Ejecutable. Menú principal.
* funciones_adicionales.py    # Módulo de funciones genéricas.
* funciones_agenda.py         # Módulo de funciones para manipular la agenda.
* agenda.csv                  # Archivo donde se guardan los contactos.
* agenda_contactos.log        # Archivo de logs.
* requirements.txt            # Módulos necesarios.
