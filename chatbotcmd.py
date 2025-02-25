import menu
import pedidos
from datetime import datetime

ingredientes_pizzas = {
    "Margarita": "Tomate, mozzarella y albahaca",
    "Pepperoni": "Tomate, mozzarella y pepperoni",
    "Cuatro Quesos": "Mozzarella, gorgonzola, parmesano y emmental",
    "Hawaiana": "Tomate, mozzarella, jamón y piña",
    "Barbacoa": "Tomate, mozzarella, carne, cebolla y salsa barbacoa",
    "Vegetariana": "Tomate, mozzarella, champiñones, pimientos y aceitunas"
}

def mostrar_pedido_actual(pedido_actual):
    print("\n\033[1;34m📌 Tu pedido actual:\033[0m")
    total = 0
    for pizza, precio in pedido_actual:
        print(f"  🍕 {pizza} - ${precio:.2f}")
        total += precio
    print(f"\n\033[1;32m💰 Total: ${total:.2f}\033[0m")

def iniciar_chatbot():
    print("\n\033[1;33m¡Bienvenido a la Pizzería! 🍕\033[0m")
    nombre_usuario = input("\033[1mPor favor, ingresa tu nombre: \033[0m").strip()
    
    pedido_actual = []
    while True:
        print("\n\033[1;36m¿Qué deseas hacer?\033[0m")
        print("1. Pedir pizza")
        print("2. Ver ingredientes de una pizza")
        print("3. Confirmar pedido")
        print("4. Salir")
        
        opcion = input("\033[1mElige una opción (1/2/3/4): \033[0m").strip()
        
        if opcion == "4":
            print("\033[1;31mGracias por visitarnos. ¡Hasta pronto!\033[0m")
            break
        
        elif opcion == "2":
            print("\n--- Ver Ingredientes ---")
            menu.mostrar_menu()
            pizza = input("Elige el número de la pizza para ver sus ingredientes: ").strip()
            
            pizzas_lista = list(ingredientes_pizzas.keys())
            if pizza.isdigit() and 1 <= int(pizza) <= len(pizzas_lista):
                seleccion = pizzas_lista[int(pizza) - 1]
                print(f"\033[1;35mLa pizza {seleccion} lleva: {ingredientes_pizzas[seleccion]}\033[0m")
            else:
                print("\033[1;31mOpción inválida. Intenta de nuevo.\033[0m")
        
        elif opcion == "1":
            print("\n--- Pedir Pizza ---")
            menu.mostrar_menu()
            pizza = input("Elige el número de la pizza que deseas ordenar: ").strip()
            
            pizzas_lista = list(menu.menu_pizzas.keys())
            if pizza.isdigit() and 1 <= int(pizza) <= len(pizzas_lista):
                seleccion = pizzas_lista[int(pizza) - 1]
                precio = menu.menu_pizzas[seleccion]
                print(f"\033[1;32m✅ Has añadido {seleccion}. Precio: ${precio:.2f}\033[0m")
                pedido_actual.append((seleccion, precio))
                mostrar_pedido_actual(pedido_actual)
            else:
                print("\033[1;31mOpción inválida. Intenta de nuevo.\033[0m")
        
        elif opcion == "3":
            if not pedido_actual:
                print("\033[1;31mNo tienes pizzas en tu pedido. Añade alguna antes de confirmar.\033[0m")
                continue
            
            mostrar_pedido_actual(pedido_actual)
            confirmar = input("\033[1m¿Confirmas tu pedido? (1: Sí / 2: No): \033[0m").strip()
            if confirmar == "1":
                hora_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lista_pizzas_pedido = [p for p, _ in pedido_actual]
                pedidos.guardar_pedido(nombre_usuario, lista_pizzas_pedido, hora_pedido)
                print(f"\n\033[1;32m Pedido confirmado. ¡Gracias por tu compra, {nombre_usuario}!\033[0m")
                break
            else:
                print("\033[1;31mPedido cancelado. Puedes seguir añadiendo pizzas o salir.\033[0m")
        else:
            print("\033[1;31mOpción no válida. Por favor, intenta de nuevo.\033[0m")

if __name__ == "__main__":
    iniciar_chatbot()
