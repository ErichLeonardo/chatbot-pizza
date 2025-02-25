# 🍕🏨 Chatbots de Pizzería y Reservas de Hotel en Terminal

Este es un chatbot interactivo basado en terminal que permite a los usuarios realizar pedidos de pizza o reservar una habitación en un hotel de manera sencilla y rápida.

## 🚀 Características
### 🍕 Chatbot de Pizzería
- Pedir una o varias pizzas en un solo pedido.
- Ver la lista de ingredientes de cada pizza antes de decidir.
- Mostrar el pedido en tiempo real con el precio total.
- Confirmar o cancelar el pedido antes de finalizar.
- Estilizado en la terminal con colores para mejorar la experiencia visual.

### 🏨 Chatbot de Reservas de Hotel
- Reservar una habitación seleccionando tipo y número de noches.
- Ver detalles de cada tipo de habitación antes de decidir.
- Ingresar una fecha de entrada válida en formato **DD/MM/YYYY**.
- Validación para evitar fechas pasadas o reservas en 2024.
- Confirmar o cancelar la reserva antes de finalizar.
- Guardar las reservas en un archivo **JSON**.

## 🛠 Requisitos
- **Python 3.x**

## 📥 Instalación
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/chatbot-reservas-pizza.git
   ```
2. Entrar en la carpeta del proyecto:
   ```sh
   cd chatbot-reservas-pizza
   ```

## ▶️ Uso
### 🍕 Para ejecutar el Chatbot de Pizzería
```sh
python chatbot_pizza.py
```
Luego, sigue las instrucciones en la pantalla para hacer tu pedido.

### 🏨 Para ejecutar el Chatbot de Reservas de Hotel
```sh
python chatbot_hotel.py
```
Luego, sigue las instrucciones en la pantalla para hacer tu reserva.

## 📋 Menú de Pizzas
1. Margarita: **Tomate, mozzarella y albahaca**
2. Pepperoni: **Tomate, mozzarella y pepperoni**
3. Cuatro Quesos: **Mozzarella, gorgonzola, parmesano y emmental**
4. Hawaiana: **Tomate, mozzarella, jamón y piña**
5. Barbacoa: **Tomate, mozzarella, carne, cebolla y salsa barbacoa**
6. Vegetariana: **Tomate, mozzarella, champiñones, pimientos y aceitunas**

## 🏨 Tipos de Habitaciones
1. **Habitación Individual** - Cama sencilla, WiFi, TV, baño privado ($50/noche).
2. **Habitación Doble** - Cama doble, WiFi, TV, baño privado, desayuno incluido ($80/noche).
3. **Suite** - Cama king-size, WiFi, TV, sala de estar, minibar, jacuzzi ($150/noche).

## 📝 Funcionalidad
### 🍕 Chatbot de Pizzería
1. **Pedir Pizza**: Selecciona una pizza ingresando el número correspondiente.
2. **Ver Ingredientes**: Consulta los ingredientes antes de decidir.
3. **Confirmar Pedido**: Ve el resumen del pedido antes de confirmar.
4. **Salir**: Finaliza el chatbot en cualquier momento.

### 🏨 Chatbot de Reservas de Hotel
1. **Reservar una habitación**: Selecciona el tipo y número de noches.
2. **Ver detalles**: Consulta los detalles de cada tipo de habitación.
3. **Confirmar Reserva**: Ve el resumen de la reserva antes de confirmar.
4. **Salir**: Finaliza el chatbot en cualquier momento.

## 📦 Contribución
Si deseas mejorar el chatbot, siéntete libre de contribuir:
1. **Realiza un fork** del repositorio.
2. **Crea una nueva rama** con tu mejora:
   ```sh
   git checkout -b mejora-nueva
   ```
3. **Realiza un commit** de tus cambios:
   ```sh
   git commit -m "Añadida nueva funcionalidad"
   ```
4. **Sube los cambios** y crea un pull request:
   ```sh
   git push origin mejora-nueva
   ```

## ⚖️ Licencia
Este proyecto es de código abierto y está bajo la licencia MIT.

---
👨‍💻 Desarrollado con ❤️ para mejorar la experiencia de pedir pizzas y reservar hoteles en terminal.
