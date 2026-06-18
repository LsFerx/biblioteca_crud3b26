from dao.libro_dao import LibroDAO

def main():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todo()
        if len(libros) == 0:
            print("No hay elementos en la lista")
        else: 
            for libro in libros:
                print(f"{libro.id} {libro.titulo} {libro.autor} {libro.isbn} {libro.disponible}")
        print("\n Conexion exitosa con a ba")
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    main()
    