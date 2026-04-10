from colorama import Fore, Style, init
init(autoreset=True)

from service import (
    create_user,
    list_users,
    update_user,
    delete_user,
    search_user,
)

def show_menu():
    while True:
        print("\n" + Fore.CYAN + "--- MENÚ PRINCIPAL ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Generar usuarios de prueba")
        print("0. Salir")

        option = input("Elige una opción: ").strip()

        # VALIDACIÓN BÁSICA
        if not option.isdigit():
            print(Fore.RED + "Debe ingresar un número")
            continue

        # ───────────── CREAR ─────────────
        if option == "1":
            try:
                name = input("Nombre: ")
                email = input("Correo: ")
                age = input("Edad: ")
                role = input("Rol: ")

                user_data = {
                    "name": name,
                    "email": email,
                    "age": age,
                    "role": role
                }

                user = create_user(user_data)
                print(Fore.GREEN + f"Usuario creado con ID: {user['id']}")

            except ValueError as e:
                print(Fore.RED + f"Error: {e}")

        # ───────────── LISTAR ─────────────
        elif option == "2":
            users = list_users()

            if not users:
                print(Fore.YELLOW + "No hay usuarios")
            else:
                for u in users:
                    print(Fore.CYAN + f"""
ID: {u['id']}
Nombre: {u['name']}
Email: {u['email']}
Edad: {u['age']}
Rol: {u['role']}
-----------------------
""")

        # ───────────── BUSCAR ─────────────
        elif option == "3":
            user_id = input("ID: ")
            user = search_user(user_id)

            if user:
                print(Fore.GREEN + f"""
Usuario encontrado:
ID: {user['id']}
Nombre: {user['name']}
Email: {user['email']}
Edad: {user['age']}
Rol: {user['role']}
""")
            else:
                print(Fore.RED + "Usuario no encontrado")

        # ───────────── ACTUALIZAR ─────────────
        elif option == "4":
            try:
                user_id = input("ID a actualizar: ")
                name = input("Nuevo nombre (opcional): ")
                age = input("Nueva edad (opcional): ")
                role = input("Nuevo rol (opcional): ")

                new_data = {}

                if name:
                    new_data["name"] = name
                if age:
                    new_data["age"] = int(age)
                if role:
                    new_data["role"] = role

                if update_user(user_id, new_data):
                    print(Fore.GREEN + "Usuario actualizado")
                else:
                    print(Fore.RED + "Usuario no encontrado")

            except ValueError as e:
                print(Fore.RED + f"Error: {e}")

        # ───────────── ELIMINAR ─────────────
        elif option == "5":
            user_id = input("ID a eliminar: ")

            if delete_user(user_id):
                print(Fore.GREEN + "Usuario eliminado")
            else:
                print(Fore.RED + "Usuario no encontrado")

        # ───────────── GENERAR USUARIOS FALSOS ─────────────
        elif option == "6":
            from integration import generate_fake_users
            users = generate_fake_users(10)
            if users:
                print(Fore.GREEN + f"Se generaron {len(users)} usuarios de prueba.")

        # ───────────── SALIR ─────────────
        elif option == "0":
            print(Fore.CYAN + "Hasta luego")
            break

        else:
            print(Fore.RED + "Opción inválida")
