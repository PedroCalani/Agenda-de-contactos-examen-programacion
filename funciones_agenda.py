# Importar módulos.
import logging
from colorama import Fore
import pandas as pd
import funciones_adicionales as f


def visualizar(df_agenda):
    """
    Función para visualizar el DataFrame introducido.
    Desde este menú se accede para:
    - visualizar todos los registros.
    - Buscar solo algunos registros, por nombre.
    - Eliminar registros.

    df_agenda : DataFrame a usar.

    return : DataFrame.
    """
    
    # Si la agenda está vacia, salir.
    if df_agenda.empty:
        print(Fore.RED + "La agenda está vacia")
        logging.warning("Se intentó visualizar una agenda vacia")
        return df_agenda

    # crear una copia de la agenda.
    df_agenda2 = df_agenda

    # log.
    logging.info("Accediendo a menú para visualizar agenda")

    # Dibujar menú con opciones.
    f.print_caja(
        "Modo de visualización \n"
        "[1] agenda completa \n"
        "[2] buscar contacto \n"
        "[3] salir"
    )
    # Elección del usuario.
    seleccion = f.input_personalizado(n_min=0, n_max=4, texto="Opción: ")

    # 3. salir.
    if seleccion == 3:
        logging.info("Operación cancelada")
        print(Fore.RED + "Operación cancelada")
        return df_agenda
    # 2. Se solicita un input para filtrar por nombre en el DataFrame df_agenda2
    elif seleccion == 2:
        filtrar = input(Fore.YELLOW + "Buscar: ")
        df_agenda2 = df_agenda2[df_agenda2["nombre"].str.contains(filtrar, case=False, na=False)]
        logging.info(f"filtro [{filtrar}] activado")
    
    # 1 y 2. Se visualizan los datos.
    contactos_por_pagina = 5
    total_contactos = len(df_agenda2)
    total_paginas = (total_contactos -1) // contactos_por_pagina + 1
    pagina = 0

    while True:
        # Calcular que contactos van en esta página.
        inicio = pagina * contactos_por_pagina
        fin = inicio + contactos_por_pagina

        # Dibujar título de página.
        print(Fore.CYAN + "-"*35)
        print(Fore.GREEN + f"Página: {pagina+1}/{total_paginas}")
        print(Fore.CYAN + "-"*35)

        # Mostrar contactos.
        print(Fore.YELLOW + df_agenda2.iloc[inicio:fin].to_string(index=False))
        logging.info(f"Visualizando página {pagina+1} de {total_paginas}")

        # Dibujar opciones.
        print(Fore.GREEN + "[id] selecciona un contacto")
        print(Fore.CYAN + "[s] Siguiente página")
        print(Fore.GREEN + "[a] anterior página")
        print(Fore.CYAN + "[m] volver al menú")

        # Opción del usuario.
        seleccion = f.input_personalizado(n_min=0, n_max=df_agenda["id"].max(), letras_validas=["s", "a", "m"])

        # s. para ir a la siguiente página. Si no hay, va a la primera.
        if seleccion == "s":
            pagina += 1
            if pagina >= total_paginas:
                pagina = 0
        # a. para ir a la anterior página. Si no hay, va a la última.
        elif seleccion == "a":
            pagina -= 1
            if pagina <= 0:
                pagina = total_paginas-1
        # m. para ir al menú.
        elif seleccion == "m":
            return df_agenda
        
        # [id] para seleccionar un contacto del listado.
        elif seleccion > 0:
            # Si afirmativamente ese contacto existe.
            if seleccion in df_agenda["id"].values:
                # Modificar el contacto.
                df_agenda = modificar_contacto(df_agenda, seleccion)
                return df_agenda
            # Si no existe, notificarlo.
            else:
                print(Fore.RED + f"El contacto {seleccion} no existe")
                logging.info("Se intentó seleccionar un contacto inexistente.")


def modificar_contacto(df_agenda, id):
    """
    Funcion para modificar un elemento/contacto de un DataFrame.
    Permite editar el registro, o eliminarlo totalmente.

    df_agenda : DataFrame.
    id : "id" del registro a tratar.

    return : DataFrame.
    """
    
    # Localizar en el DataFrame.
    c_seleccionado = df_agenda[df_agenda["id"] == id].iloc[0]
    logging.info(f"Contacto id:{id} nombre:{c_seleccionado} seleccionado")

    # Dibujar opciones.
    print(Fore.GREEN + f"¿Qué hacer con el contacto {c_seleccionado['nombre']}?")
    print(Fore.CYAN + "[1] editar")
    print("[2] eliminar")
    # Solicitar elección.
    accion = f.input_personalizado(n_min=0, n_max=3)

    # Cambiar la información del contacto seleccionado.
    if accion == 1:
        print(Fore.BLUE + f"EDITAR CONTACTO {c_seleccionado['nombre']}")
        print(Fore.BLACK + "Deja un campo vacio si no quieres modificarlo")

        c_nombre = input(Fore.YELLOW + "Nuevo Nombre: ")
        if c_nombre == "":
            c_nombre = c_seleccionado['nombre']

        c_numero = f.input_numerico(texto="Nuevo Número: ")
        if c_numero == 0:
            c_numero = c_seleccionado['numero']

        c_correo = input(Fore.YELLOW + "Nuevo Correo: ")
        if c_correo == "":
            c_correo = c_seleccionado['correo']

        logging.info(f"Contacto id:{id} nombre:{c_seleccionado['nombre']} será modificado")
        df_agenda.loc[df_agenda["id"] == id, ["nombre", "numero", "correo"]] = [c_nombre, c_numero, c_correo]

        print(Fore.RED + f"Contacto id:{id} nombre:{c_seleccionado['nombre']} MODIFICADO")
        logging.info(f"Contacto id:{id} nombre:{c_seleccionado['nombre']} MODIFICADO")

        return df_agenda

    # Eliminar el contacto del DataFrame.
    elif accion == 2:
        df_agenda = df_agenda.drop(df_agenda[df_agenda["id"] == id].index)
        logging.info(f"Contacto id:{id} nombre:{c_seleccionado} ELIMINADO")
        print(Fore.RED + "Contacto eliminado")
        return df_agenda


def crear_contacto(df_agenda):
    """
    Crea un contacto nuevo.

    df_agenda : DataFrame donde se crea el contacto.

    return : DataFrame.
    """
    
    print(Fore.GREEN + "| CREAR NUEVO CONTACTO |")
    # Si no hay contactos, el id es 1.
    if df_agenda.empty:
        c_id = 1
    # Si no, asigna el id correspondiente.
    else:
        c_id = df_agenda["id"].max()+1

    # Solicitar datos.
    c_nombre = input(Fore.YELLOW + "Nombre: ")
    c_numero = f.input_numerico(texto="Número: ")
    c_correo = input(Fore.YELLOW + "Correo: ")

    # Crear un DataFrame que se concatenará con el original.
    contacto_nuevo = pd.DataFrame([{
        "id" : c_id,
        "nombre" : c_nombre,
        "numero" : c_numero,
        "correo" : c_correo
    }])

    # Agregar contacto.
    df_agenda = pd.concat([df_agenda, contacto_nuevo], ignore_index=True)

    print(Fore.LIGHTYELLOW_EX + f"Contacto [{c_nombre}] creado")
    logging.info(f"Nuevo contacto id:{c_id} nombre:{c_nombre} creado")

    return df_agenda

