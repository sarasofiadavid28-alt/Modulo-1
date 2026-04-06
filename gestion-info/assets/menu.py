# main.py

# ==============================
# SISTEMA DE GESTIÓN DE VENTAS
# Módulo 0 + Módulo 1
# ==============================

import os

# ------------------------------
# ESTRUCTURAS DE DATOS
# ------------------------------
ventas = []
ids = set()

# ------------------------------
# FUNCIONES
# ------------------------------

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def validar_id(id_venta):
    if id_venta in ids:
        print(" Error: El ID ya existe.")
        return False
    return True


def crear_venta():
    print("\n--- CREAR VENTA ---")
    
    try:
        id_venta = int(input("ID de la venta: "))
        
        if not validar_id(id_venta):
            return
        
        producto = input("Producto: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        cliente = input("Tipo de cliente (normal/vip): ").strip().lower()
        estado = input("Estado (ok/cancelado): ").strip().lower()

        venta = {
            "id": id_venta,
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad,
            "cliente": cliente,
            "estado": estado
        }

        ventas.append(venta)
        ids.add(id_venta)

        print(" Venta registrada correctamente.")

    except ValueError:
        print("Error: Datos inválidos. Intente nuevamente.")


def listar_ventas():
    print("\n--- LISTA DE VENTAS ---")
    
    if not ventas:
        print("No hay ventas registradas.")
        return

    for v in ventas:
        print(f"""
ID: {v['id']}
Producto: {v['producto']}
Precio: {v['precio']}
Cantidad: {v['cantidad']}
Cliente: {v['cliente']}
Estado: {v['estado']}
--------------------------
""")


# ------------------------------
# MENÚ PRINCIPAL
# ------------------------------

def menu():
    while True:
        limpiar_pantalla()
        
        print("=" * 50)
        print("SISTEMA DE GESTIÓN DE VENTAS")
        print("=" * 50)
        print("1. Crear venta")
        print("2. Listar ventas")
        print("3. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_venta()
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            listar_ventas()
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            print("\n Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
            input("\nPresione Enter para continuar...")


# ------------------------------
# PUNTO DE ENTRADA
# ------------------------------

if __name__ == "__main__":
    print("Sistema listo 🚀")
    input("Presione Enter para iniciar...")
    menu()
