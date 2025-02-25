import json

archivo_pedidos = "pedidos.json"

def guardar_pedido(nombre, lista_pizzas, hora):
    try:
        with open(archivo_pedidos, "r") as archivo:
            pedidos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        pedidos = []
    
    pedido = {"nombre": nombre, "pizzas": lista_pizzas, "hora": hora}
    pedidos.append(pedido)
    
    with open(archivo_pedidos, "w") as archivo:
        json.dump(pedidos, archivo, indent=4)

def mostrar_pedidos():
    try:
        with open(archivo_pedidos, "r") as archivo:
            pedidos = json.load(archivo)
            if pedidos:
                print("\n--- Pedidos Confirmados ---")
                for pedido in pedidos:
                    pizzas_texto = ", ".join(pedido['pizzas'])
                    print(f"Cliente: {pedido['nombre']} - Pizzas: {pizzas_texto} - Hora: {pedido['hora']}")
            else:
                print("No hay pedidos registrados.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay pedidos registrados.")

if __name__ == "__main__":
    mostrar_pedidos()
