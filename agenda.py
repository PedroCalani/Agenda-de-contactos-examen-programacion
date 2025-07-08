#importar modulos.
import logging
import os

from colorama import init, Fore
import pandas as pd

import funciones_adicionales as f
import funciones_agenda as fa

# Iniciar colorama.
init()

# ruta de esta carpeta.
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Archivo .log para los registros.
ruta_log = os.path.join(ruta_actual, "agenda_contactos.log")
logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Archivo .csv agenda
ruta_csv = os.path.join(ruta_actual, "agenda.csv")

# leer .csv de la agenda de contactos
df_agenda = pd.read_csv(ruta_csv)


def iniciar_agenda():
    """
    Iniciar agenda.
    Abre el menú principal en consola.
    Desde este menú se puede:
    - Ver contactos -> para ver/buscar/editar/eliminar uno.
    - Crear nuevo contacto -> Agrega un contacto a la agenda.
    """

    # log.
    logging.info("Agenda de contactos iniciada")

    # para que la funcion reconozca el DataFrame de la agenda.
    global df_agenda

    while True:

        # Dibujar menú en consola.
        f.print_caja(
            "AGENDA DE CONTACTOS \n"
            "[1] ver contactos \n"
            "[2] crear nuevo contacto \n"
            "[3] cerrar agenda"
        )

        # Elección del usuario.
        seleccion = f.input_personalizado(n_min=0, n_max=4, texto="Ir a: ")

        # Opción para visualizar la agenda.
        if seleccion == 1:
            df_agenda = fa.visualizar(df_agenda)
            df_agenda.to_csv(ruta_csv, index=False)
            logging.info("agenda.csv guardado")

        # Opción para crear un nuevo contacto.
        elif seleccion == 2:
            df_agenda = fa.crear_contacto(df_agenda)
            df_agenda.to_csv(ruta_csv, index=False)
            logging.info("agenda.csv guardado")
        
        # Opción para salir.
        elif seleccion == 3:
            # Resetea los id de los contactos por si alguno quedó vacio.
            df_agenda = df_agenda.reset_index(drop=True)
            df_agenda["id"] = df_agenda.index +1
            df_agenda.to_csv(ruta_csv, index=False)
            logging.info("agenda.csv guardado")

            logging.info("Agenda de contactos finalizada")
            exit()


# Ejecutar la agenda.
iniciar_agenda()
