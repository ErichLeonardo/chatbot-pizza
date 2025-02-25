import json
import datetime

archivo_reservas = "reservas.json"

def guardar_reserva(nombre, tipo_habitacion, fecha_inicio, noches, total):
    try:
        with open(archivo_reservas, "r") as archivo:
            reservas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        reservas = []
    
    fecha_inicio_dt = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
    fecha_salida_dt = fecha_inicio_dt + datetime.timedelta(days=noches)
    fecha_salida = fecha_salida_dt.strftime("%d/%m/%Y")
    
    nueva_reserva = {
        "nombre": nombre,
        "tipo_habitacion": tipo_habitacion,
        "fecha_entrada": fecha_inicio,
        "fecha_salida": fecha_salida,
        "noches": noches,
        "total": total
    }
    
    reservas.append(nueva_reserva)
    
    with open(archivo_reservas, "w") as archivo:
        json.dump(reservas, archivo, indent=4)

def mostrar_reservas():
    try:
        with open(archivo_reservas, "r") as archivo:
            reservas = json.load(archivo)
            if reservas:
                print("\n--- Reservas Confirmadas ---")
                for reserva in reservas:
                    print(f"Cliente: {reserva['nombre']} - Habitación: {reserva['tipo_habitacion']} - Desde: {reserva['fecha_entrada']} hasta {reserva['fecha_salida']} - Noches: {reserva['noches']} - Total: ${reserva['total']:.2f}")
            else:
                print("No hay reservas registradas.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay reservas registradas.")

def iniciar_chatbot():
    print("\n\033[1;33m¡Bienvenido al Chatbot de Reservas de Hotel! 🏨\033[0m")
    nombre_usuario = input("\033[1mPor favor, ingresa tu nombre: \033[0m").strip()
    
    reserva_actual = {}
    
    while True:
        print("\n\033[1;36m¿Qué deseas hacer?\033[0m")
        print("1. Reservar una habitación")
        print("2. Ver detalles de la habitación")
        print("3. Confirmar reserva")
        print("4. Salir")
        
        opcion = input("\033[1mElige una opción (1/2/3/4): \033[0m").strip()
        
        if opcion == "4":
            print("\033[1;31mGracias por visitarnos. ¡Hasta pronto!\033[0m")
            break
        
        elif opcion == "1":
            print("\n🏨 Tipos de habitaciones disponibles:")
            print("1. Habitación Individual - $50/noche")
            print("2. Habitación Doble - $80/noche")
            print("3. Suite - $150/noche")
            
            habitacion = input("Selecciona el número de la habitación que deseas reservar: ").strip()
            
            precios = {"1": 50, "2": 80, "3": 150}
            tipos = {"1": "Habitación Individual", "2": "Habitación Doble", "3": "Suite"}
            
            if habitacion in precios:
                fecha_inicio = input("Ingresa la fecha de entrada (formato: DD/MM/YYYY, ejemplo: 01/06/2025): ").strip()
                try:
                    fecha_inicio_dt = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
                    noches = int(input("¿Cuántas noches deseas reservar?: ").strip())
                    total = precios[habitacion] * noches
                    fecha_salida_dt = fecha_inicio_dt + datetime.timedelta(days=noches)
                    fecha_salida = fecha_salida_dt.strftime("%d/%m/%Y")
                    
                    reserva_actual = {
                        "nombre": nombre_usuario,
                        "tipo_habitacion": tipos[habitacion],
                        "fecha_entrada": fecha_inicio,
                        "fecha_salida": fecha_salida,
                        "noches": noches,
                        "total": total
                    }
                    print(f"\033[1;32m✅ Reserva pendiente: {tipos[habitacion]} desde {fecha_inicio} hasta {fecha_salida}. Total: ${total:.2f}\033[0m")
                except ValueError:
                    print("⚠️ Formato inválido. Usa DD/MM/YYYY.")
            else:
                print("\033[1;31mOpción inválida. Intenta de nuevo.\033[0m")
        
        elif opcion == "3":
            if not reserva_actual:
                print("\033[1;31mNo tienes reservas activas. Reserva una habitación primero.\033[0m")
                continue
            
            print("\n\033[1;34m📌 Tu reserva actual:\033[0m")
            print(f"  🏨 {reserva_actual['tipo_habitacion']} - Desde {reserva_actual['fecha_entrada']} hasta {reserva_actual['fecha_salida']} - {reserva_actual['noches']} noches")
            print(f"\n\033[1;32m💰 Total: ${reserva_actual['total']:.2f}\033[0m")
            
            confirmar = input("\033[1m¿Confirmas tu reserva? (1: Sí / 2: No): \033[0m").strip()
            if confirmar == "1":
                guardar_reserva(
                    reserva_actual['nombre'],
                    reserva_actual['tipo_habitacion'],
                    reserva_actual['fecha_entrada'],
                    reserva_actual['noches'],
                    reserva_actual['total']
                )
                print(f"\n\033[1;32m🎉 Reserva confirmada para {nombre_usuario} desde {reserva_actual['fecha_entrada']} hasta {reserva_actual['fecha_salida']}.\033[0m")
                break
            else:
                print("\033[1;31mReserva cancelada. Puedes seguir reservando o salir.\033[0m")
        else:
            print("\033[1;31mOpción no válida. Por favor, intenta de nuevo.\033[0m")

if __name__ == "__main__":
    iniciar_chatbot()
