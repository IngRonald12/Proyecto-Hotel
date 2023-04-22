from os import system 
system ("cls")
# Definir una lista de habitaciones con su disponibilidad y precio por noche
habitaciones = [
    {"numero": 101, "disponible": True, "precio": 50, }, #Faltan datos para gestión
    {"numero": 102, "disponible": True, "precio": 60, },
    {"numero": 103, "disponible": True, "precio": 70, },
    {"numero": 104, "disponible": True, "precio": 80, },
    {"numero": 105, "disponible": True, "precio": 90, }
]

#Gestión de reservas

#Gestion las habitaciones ocupadas 

#datos = {101: [cedula, nombre, apellido, fechallegada, fechasalida]}

Registro_personas={1003259544:"Ronald", 2515:"Jorman"} #aumentar esos datos

datos_admin = {1065875411:["Didier guerrero", "dfguerrero", 909090]}

def eliminar():
    Delete=(input("Ingrese Dato que desea eliminar -> "))
    if Delete in Registro_personas:          
        Registro_personas.pop(Delete)
        print(f"El elemento eliminado es: {Delete}")
    elif Delete in Registro_personas:
        print(f"{Delete} No existe ")

def registro():
    print("Bienvenido al registro Hotel bella vista.")
    Documento1=int(input("Ingrese documento de identidad -> "))
    value=input("Ingrese nombre - >").lower()
    #direccion=input("Ingrese su dirección ->").lower()
    #telefono=int(input("ingrese su numero de telefono -> "))
    Registro_personas.update({Documento1:value});system("cls")
    print(f"Señor {value} usted ha sido agregado exitosamente! ")

def editar():
    nombre_edit=input("ingrese el dato que quiere editar -> ")
    if nombre_edit in Registro_personas:
        Registro_personas.update({"Documento": nombre_edit})    
    for nombre_edit in Registro_personas:
        print(Registro_personas)

def login(): #usuario administrador
    while True:
        inicio=(input("¿Está usted registrado si/no? -> ")).lower();system("cls")
        if inicio=="si":
            usuario = int(input("Ingrese su documento de identidad ->"))
            if usuario==datos_admin:
                print("BIENVENIDO")
            print("---------------------------");print(datos_admin[usuario]), print("---------------------------")
        if inicio== "no":
            print("Usted no es administrador ")
        break

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
            print("--------------------------------------------------")
            print(f'Reservaste la habitación {numero_habitacion} para {personas} personas')
            print("--------------------------------------------------")
            print(f"por {noches} noches. Total a pagar: {total} dolares ")
            print("--------------------------------------------------")
            return
    print(f'Lo siento, la habitación {numero_habitacion} no está disponible.')

login()

while True:
        print("Menú:")
        print("1. Agregar elemento") #? especificar que?
        print("2. Editar elemento")
        print("3. Eliminar elemento")
        print("4. Realizar una reserva ")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        system ("cls")
        while True:
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
                personas=int(input("Ingrese la cantidad de personas ->"));system("cls")
                hacer_reserva(numero_habitacion, noches, personas)
                break
            if opcion=="5":
                print("Cerrando programa...")
                break
        break