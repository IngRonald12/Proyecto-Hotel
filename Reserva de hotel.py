from os import system 
system ("cls")
# Definir una lista de habitaciones con su disponibilidad y precio por noche
habitaciones = [
    {"numero": 101, "disponible": True, "precio": 50, },
    {"numero": 102, "disponible": True, "precio": 60, },
    {"numero": 103, "disponible": True, "precio": 70, },
    {"numero": 104, "disponible": True, "precio": 80, },
    {"numero": 105, "disponible": True, "precio": 90, }
]

Registro_personas={1003259544:"Ronald", 2515:"Jorman"} 

def eliminar():
    del Registro_personas["Documento"]

def registro():
    print("Bienvenido al registro Hotel bella vista.")
    keys =int(input("Ingrese documento de identidad -> "))
    value=input("Ingrese nombre - >")
    Registro_personas[keys]=value


def editar():
    nombre_edit=input("ingrese el dato que quiere editar -> ")
    Registro_personas.update({"Documento": nombre_edit})

def login():
    usuario = int(input("Ingrese su documento de identidad ->"))
    if Registro_personas[usuario]:
        print("BIENVENIDO")
        print("---------------------------");print(Registro_personas[usuario]), print("---------------------------")

#Función para mostrar las habitaciones disponibles
def mostrar_habitaciones():
    for habitacion in habitaciones:
        if habitacion["disponible"]:
            print(f'Habitación {habitacion["numero"]} - precio por noche: {habitacion["precio"]}')
# Función para hacer una reserva
def hacer_reserva(numero_habitacion, noches, personas):
    for habitacion in habitaciones:
        if habitacion["numero"] == numero_habitacion and habitacion["disponible"]:
            habitacion["disponible"] = False
            total = habitacion["precio"] * noches
            print("---------------------------------------------------------------------------------------")
            print(f'Reservaste la habitación {numero_habitacion} para {personas} personas por {noches} noches. Total a pagar: {total}')
            print("---------------------------------------------------------------------------------------")
            return
    print(f'Lo siento, la habitación {numero_habitacion} no está disponible.')


while True:
        print("Menú:")
        print("1. Agregar elemento")
        print("2. Editar elemento")
        print("3. Eliminar elemento")
        print("4. hacer una reserva ")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
    
        if opcion == "1":
            registro()
        if opcion=="2":
            editar()
        if opcion=="3":
            eliminar()
        if opcion== "4":
            Nombre=input("ingrese su nombre -> ")
            documento=int(input("Ingrese su documento de identidad -> "))
            mostrar_habitaciones()
            numero_habitacion = int(input("Ingresa el número de la habitación que deseas reservar: "))
            noches = int(input("Ingresa el número de noches que te quedarás: "))
            personas=int(input("Ingrese la cantidad de personas ->"))
            hacer_reserva(numero_habitacion, noches, personas)
            break
        if opcion=="5":
            print("Cerrando programa...")
            break
