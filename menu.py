menu_pizzas = {
    "1. Margarita": 8.99,
    "2. Pepperoni": 10.99,
    "3. Cuatro Quesos": 11.99,
    "4. Hawaiana": 9.99,
    "5. Barbacoa": 12.49,
    "6. Vegetariana": 9.49
}

ingredientes_pizzas = {
    "1. Margarita": "Tomate, mozzarella y albahaca",
    "2. Pepperoni": "Tomate, mozzarella y pepperoni",
    "3. Cuatro Quesos": "Mozzarella, gorgonzola,\nparmesano y emmental",
    "4. Hawaiana": "Tomate, mozzarella, jamón y piña",
    "5. Barbacoa": "Tomate, mozzarella, carne,\ncebolla y salsa barbacoa",
    "6. Vegetariana": "Tomate, mozzarella,\nchampiñones, pimientos y aceitunas"
}


def mostrar_menu():
    print("\n--- Menú de Pizzas ---")
    for pizza, precio in menu_pizzas.items():
        print(f"{pizza}: ${precio:.2f}")

if __name__ == "__main__":
    mostrar_menu()
