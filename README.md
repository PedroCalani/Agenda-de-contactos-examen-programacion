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

Podés crear un entrono virtual para instalar lo módulos o hacerlo directamente en tu espacio personal.
Instalá los módulos mencionados en requirements.txt

Ejecutá agenda.py

El manejo de la agenda es realizado completamente mediante inputs, generalmente con valores numéricos.

## Estructura del proyecto
* agenda.py                   # Ejecutable. Menú principal.
* funciones_adicionales.py    # Módulo de funciones genéricas.
* funciones_agenda.py         # Módulo de funciones para manipular la agenda.
* agenda.csv                  # Archivo donde se guardan los contactos.
* agenda_contactos.log        # Archivo de logs.
* requirements.txt            # Módulos necesarios.
