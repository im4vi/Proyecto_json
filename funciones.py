import json
import os

# Función para cargar los datos desde el archivo JSON
def cargar_datos(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':  # Si el sistema es Windows
        os.system('cls')
    else:  # Si el sistema es Linux o macOS
        os.system('clear')

# 1. Listar los nombres de los clubes
def listar_clubes(datos):
    limpiar_pantalla()  # Limpiar pantalla antes de mostrar los resultados
    print("Lista de clubes en LaLiga:")
    for club in datos['clubs']:
        print(f"- {club['nombre']}")
    input("Presiona Enter para volver al menú...")  # Esperar que el usuario presione Enter

# 2. Contar el número total de clubes
def contar_clubes(datos):
    limpiar_pantalla()
    total_clubes = len(datos['clubs'])
    print(f"Total de clubes en LaLiga: {total_clubes}")
    input("Presiona Enter para volver al menú...")

# 3. Buscar clubes por una subcadena en su nombre
def buscar_clubes_por_nombre(datos, subcadena):
    limpiar_pantalla()
    print(f"Clubes que contienen '{subcadena}' en su nombre:")
    encontrados = [club['nombre'] for club in datos['clubs'] if subcadena.lower() in club['nombre'].lower()]
    if encontrados:
        for club in encontrados:
            print(f"- {club}")
    else:
        print("No se encontraron clubes con esa subcadena.")
    input("Presiona Enter para volver al menú...")

# 4. Buscar información relacionada: Mostrar estadio de un club por su código
def mostrar_club_por_codigo(datos, codigo):
    limpiar_pantalla()
    for club in datos['clubs']:
        if club['codigo'].upper() == codigo.upper():
            print(f"El codigo '{codigo}' pertenece al club {club['nombre']}, que juega en el estadio {club['estadio']}.")
            input("Presiona Enter para volver al menú...")
            return
    print(f"No se encontró ningun club con el codigo '{codigo}'.")
    input("Presiona Enter para volver al menú...")

# 5. Listar clubes ordenados por año de fundación
def listar_clubes_por_antiguedad(datos):
    limpiar_pantalla()
    clubes_ordenados = sorted(datos['clubs'], key=lambda x: x['fundacion'])
    print("Lista de clubes ordenados por año de fundación:")
    for club in clubes_ordenados:
        print(f"- {club['nombre']} (Fundado en {club['fundacion']})")
    input("Presiona Enter para volver al menú...")
