from funciones import cargar_datos, listar_clubes, contar_clubes, buscar_clubes_por_nombre, mostrar_club_por_codigo, listar_clubes_por_antiguedad

# Función para mostrar el menú y ejecutar las opciones
def menu():
    ruta_archivo = 'datos/clubs.json'  # Ruta al JSON
    datos = cargar_datos(ruta_archivo)

    while True:
        # Menú interactivo
        print(" MENU DE OPCIONES ")
        print("1. Listar los nombres de los clubes")
        print("2. Contar el número total de clubes")
        print("3. Buscar clubes por una subcadena en su nombre")
        print("4. Buscar información relacionada (estadio por código)")
        print("5. Listar clubes ordenados por año de fundación")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            listar_clubes(datos)
        elif opcion == '2':
            contar_clubes(datos)
        elif opcion == '3':
            subcadena = input("Ingrese una subcadena para buscar clubes: ")
            buscar_clubes_por_nombre(datos, subcadena)
        elif opcion == '4':
            codigo = input("Ingrese el codigo de un club para obtener su estadio: ")
            mostrar_club_por_codigo(datos, codigo)
        elif opcion == '5':
            listar_clubes_por_antiguedad(datos)
        elif opcion == '6':
            print("¡Hasta luego!")
            break  # Salir del bucle y finalizar el programa
        else:
            print("Opcion no valida. Por favor, selecciona una opcion entre 1 y 6.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
