from service import (
    create_user,
    list_users,
    update_user,
    delete_user,
)

users = []
ids = set()


def show_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Salir")

        option = input("Elige una opción: ").strip()

        if option == "1":
            try:
                id_user = int(input("ID: "))
                name = input("Nombre: ")
                email = input("Correo: ")

                user = {
                    "id": id_user,
                    "name": name,
                    "email": email
                }

                if create_user(users, ids, user):
                    print("Usuario creado")
                else:
                    print("ID duplicado")

            except ValueError:
                print("Datos inválidos")

        elif option == "2":
            data = list_users(users)
            for u in data:
                print(u)

        elif option == "3":
            try:
                id_user = int(input("ID a actualizar: "))
                name = input("Nuevo nombre: ")

                if update_user(users, id_user, {"name": name}):
                    print("Actualizado")
                else:
                    print("Usuario no encontrado")

            except ValueError:
                print("Error")

        elif option == "4":
            try:
                id_user = int(input("ID a eliminar: "))
                users[:] = delete_user(users, id_user)
                print("Eliminado")
            except ValueError:
                print("Error")

        elif option == "0":
            print("Hasta luego")
            break

        else:
            print("Opción inválida")
