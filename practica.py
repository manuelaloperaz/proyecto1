
libros = []

# Función para agregar un libro a la lista
def agregar_libro(nombre, autor, editorial, genero):
    libro = {
        'nombre': nombre,
        'autor': autor,
        'editorial': editorial,
        'genero': genero
    }
    libros.append(libro)

# Función para mostrar todos los libros
def mostrar_libros():
    if not libros:
        print("No hay libros en la lista.")
    else:
        for i, libro in enumerate(libros, 1):
            print(f"Libro {i}:")
            print(f"Nombre: {libro['nombre']}")
            print(f"Autor: {libro['autor']}")
            print(f"Editorial: {libro['editorial']}")
            print(f"Género: {libro['genero']}")
            print("")

# Función para eliminar un libro de la lista
def eliminar_libro(index):
    if 0 < index <= len(libros):
        del libros[index - 1]
        print(f"Libro {index} eliminado.")
    else:
        print("Índice inválido.")

# Menú principal
while True:
    print("Menú:")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del libro: ")
        autor = input("Autor del libro: ")
        editorial = input("Editorial del libro: ")
        genero = input("Género del libro: ")
        agregar_libro(nombre, autor, editorial, genero)
        print("Libro agregado con éxito.")
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        index = int(input("Ingrese el número de libro que desea eliminar: "))
        eliminar_libro(index)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") 
        print("")