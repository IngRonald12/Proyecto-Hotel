from os import system 
system ("cls")
# Definir una lista de habitaciones con su disponibilidad y precio por noche
habitaciones = [
    {"numero": 101, "disponible": True, "precio": 50, },
    {"numero": 102, "disponible": True, "precio": 60, },
    {"numero": 103, "disponible": True, "precio": 70, },
    {"numero": 104, "disponible": True, "precio": 80, },
    {"numero": 105, "disponible": True, "precio": 90,}
]




# Función para mostrar las habitaciones disponibles
def mostrar_habitaciones():
    for habitacion in habitaciones:
        if habitacion["disponible"]:
            print(f'Habitación {habitacion["numero"]} - precio por noche: {habitacion["precio"]}')
# Función para hacer una reserva
def hacer_reserva(numero_habitacion, noches):
    for habitacion in habitaciones:
        if habitacion["numero"] == numero_habitacion and habitacion["disponible"]:
            habitacion["disponible"] = False
            total = habitacion["precio"] * noches
            print(f'Reservaste la habitación {numero_habitacion} por {noches} noches. Total a pagar: {total}')
            return
    print(f'Lo siento, la habitación {numero_habitacion} no está disponible.')

# Mostrar registro de datos 


# Mostrar las habitaciones disponibles
print("Habitaciones disponibles:")
mostrar_habitaciones()


# Hacer una reserva
numero_habitacion = int(input("Ingresa el número de la habitación que deseas reservar: "))
noches = int(input("Ingresa el número de noches que te quedarás: "))
hacer_reserva(numero_habitacion, noches)

# Mostrar las habitaciones disponibles después de hacer la reserva
print("Habitaciones disponibles:")
mostrar_habitaciones()

