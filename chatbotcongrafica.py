import tkinter as tk
import menu
import pedidos
from datetime import datetime

pedidos_usuario = []
nombre_usuario = ""
mensaje_estado = None  # Etiqueta para mostrar mensajes en lugar de messagebox

def mostrar_mensaje(texto, color="black", tiempo=0):
    mensaje_estado.config(text=texto, fg=color)
    if tiempo > 0:
        mensaje_estado.after(tiempo, lambda: mensaje_estado.config(text=""))

def agregar_pedido():
    seleccion = lista_pizzas.curselection()
    if not seleccion:
        mostrar_mensaje("Por favor, selecciona una pizza.", "red")
        return
    
    pizza = lista_pizzas.get(seleccion[0])
    precio = menu.menu_pizzas[pizza]
    pedidos_usuario.append((pizza, precio))
    actualizar_pedido()
    mostrar_mensaje(f"{pizza} añadida al pedido.", "green")

def actualizar_pedido():
    pedido_texto.set("\n".join([f"{p} - ${c:.2f}" for p, c in pedidos_usuario]))

def confirmar_pedido():
    global nombre_usuario
    nombre_usuario = entry_nombre.get().strip()
    if not nombre_usuario:
        mostrar_mensaje("Por favor, ingresa tu nombre.", "red")
        return
    
    if not pedidos_usuario:
        mostrar_mensaje("No has seleccionado ninguna pizza.", "red")
        return
    
    total = sum(c for _, c in pedidos_usuario)
    hora_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lista_pizzas_pedido = [p for p, _ in pedidos_usuario]
    pedidos.guardar_pedido(nombre_usuario, lista_pizzas_pedido, hora_pedido)
    pedidos_usuario.clear()
    pedido_texto.set("")
    entry_nombre.delete(0, tk.END)
    mostrar_mensaje(f"Pedido confirmado por ${total:.2f}. ¡Gracias {nombre_usuario}!", "green", 10000)

def cancelar_pedido():
    global pedidos_usuario
    if not pedidos_usuario:
        mostrar_mensaje("No hay un pedido activo para cancelar.", "red")
        return
    pedidos_usuario.clear()
    pedido_texto.set("")
    mostrar_mensaje("Pedido cancelado.", "blue", 5000)

def ver_ingredientes():
    seleccion = lista_pizzas.curselection()
    if not seleccion:
        mostrar_mensaje("Por favor, selecciona una pizza.", "red")
        return
    
    pizza = lista_pizzas.get(seleccion[0])
    ingredientes = menu.ingredientes_pizzas.get(pizza, "Ingredientes no disponibles")
    mostrar_mensaje(f"Ingredientes de la pizza {pizza}: {ingredientes}", "blue", 7000)

# Configurar la ventana principal
root = tk.Tk()
root.title("Pizzería Chatbot")
root.geometry("600x700")  # Aumentar ancho de la ventana
root.configure(bg="#f4a261")

tk.Label(root, text="Bienvenido a la Pizzería", font=("Arial", 14, "bold"), bg="#f4a261", fg="white").pack(pady=10)
tk.Label(root, text="Ingresa tu nombre:", bg="#f4a261").pack()
entry_nombre = tk.Entry(root, bg="white", fg="black", width=60)
entry_nombre.pack()

tk.Label(root, text="Selecciona una pizza:", bg="#f4a261").pack()
lista_pizzas = tk.Listbox(root, bg="#ffebcd", fg="black", selectbackground="#e76f51", width=60)
for pizza in menu.menu_pizzas.keys():
    lista_pizzas.insert(tk.END, pizza)
lista_pizzas.pack()

pedido_texto = tk.StringVar()
tk.Label(root, textvariable=pedido_texto, font=("Arial", 12), fg="blue", bg="#f4a261", width=60).pack(pady=10)
mensaje_estado = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#f4a261", width=60)
mensaje_estado.pack(pady=5)

tk.Button(root, text="Añadir Pizza", command=agregar_pedido, bg="#2a9d8f", fg="white", width=40).pack(pady=5)
tk.Button(root, text="Ver Ingredientes", command=ver_ingredientes, bg="#264653", fg="white", width=40).pack(pady=5)
tk.Button(root, text="Cancelar Pedido", command=cancelar_pedido, bg="#e76f51", fg="white", width=40).pack(pady=5)
tk.Button(root, text="Confirmar Pedido", command=confirmar_pedido, bg="#e9c46a", fg="black", width=40).pack(pady=10)
tk.Button(root, text="Salir", command=root.quit, bg="#d62828", fg="white", width=40).pack(pady=10)

root.mainloop()
