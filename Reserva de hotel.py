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

#Profe hice lo que mas pude :(((
#con un 3 me conformo :(

reservaciones={}
#Gestión de reservas

#Gestion las habitaciones ocupadas 

datos = {101: ["cedula", "nombre", "fechallegada", "fechasalida"],
         102: [],
         103: [],
         104: [],
         105: []}

Registro_personas={1003259544:"Ronald", 2515:"Jorman"} #aumentar esos datos

datos_admin = {1065875411:["Didier guerrero", "dfguerrero", 909090], 1003259544:["Ronald Varela", "rvarela", 1203]}

def eliminar():
    Delete=int(input("Ingrese Dato que desea eliminar -> "))
    if Delete in Registro_personas:          
        Registro_personas.pop(Delete)
        print(f"El elemento eliminado es: {Delete}")
    elif Delete in Registro_personas:
        print(f"{Delete} No existe ")

def registro():
    print("Bienvenido al registro Hotel bella vista.")
    Documento1=int(input("Ingrese documento de identidad -> "))
    value=input("Ingrese nombre - > ").lower()
    direccion=input("Ingrese su dirección -> ").lower()
    telefono=int(input("ingrese su numero de telefono -> "))
    Registro_personas.update({"direccion":direccion})
    Registro_personas.update({"Telefono":telefono})
    Registro_personas.update({Documento1:value});system("cls")
    print(f"Señor: {value} \ndocumento: {Documento1}")
    print(f"Direccion: {direccion} \nTelefono: {telefono}")
    print("Usted ha sido registrado con exito!! ")

def editar():
    nombre_edit=input("ingrese el dato que quiere editar -> ")
    if nombre_edit in Registro_personas:
        Registro_personas.update({"Documento": nombre_edit})    
    for nombre_edit in Registro_personas:
        print(Registro_personas)

def login(): #usuario administrador
        inicio=(input("¿Está usted registrado si/no? -> ")).lower();system("cls")
        if inicio=="si":
            usuario = int(input("Ingrese su documento de identidad ->"))
            if usuario in datos_admin:
                usuario2=input("Ingrese su nombre usuario -> ").lower()
                password=input("Ingrese su contraseña -> ").lower();system ("cls")
                if usuario2 and password in datos_admin:
                    print("BIENVENIDO")
                
        if inicio== "no":
            print("Usted no es administrador ")

#Función para mostrar las habitaciones disponibles
def mostrar_habitaciones():
    for habitacion in habitaciones:
        if habitacion["disponible"]:
            print(f'Habitación {habitacion["numero"]} - precio por noche: {habitacion["precio"]}')

# Función para registrar una nueva reserva
def registrar_reserva():
    nombre = input("Ingrese el nombre del huésped: ")
    cedula = input("Ingrese la cédula del huésped: ")
    habitacion = input("Ingrese el número de la habitación: ")
    fecha_llegada = input("Ingrese la fecha de llegada (formato YYYY-MM-DD): ")
    fecha_salida = input("Ingrese la fecha de salida (formato YYYY-MM-DD): ")

    # Verificar si la habitación está disponible
    if habitacion in reservaciones:
        print(f"La habitación {habitacion} ya está reservada.")
    else:
        # Agregar la reserva al diccionario
        reservaciones[habitacion] = {
            "nombre": nombre,
            "cedula": cedula,
            "fecha_llegada": fecha_llegada,
            "fecha_salida": fecha_salida
        }
        print("Reserva registrada con éxito.")

# Función para consultar una reserva
def consultar_reserva():
    habitacion = input("Ingrese el número de la habitación para consultar:  ")
    # Verificar si la habitación está reservada
    if habitacion in reservaciones:
        datos = reservaciones[habitacion]
        print(f"Habitación {habitacion}:")
        print(f"Nombre: {datos['nombre']}")
        print(f"Cédula: {datos['cedula']}")
        print(f"Fecha de llegada: {datos['fecha_llegada']}")
        print(f"Fecha de salida: {datos['fecha_salida']}")
    else:
        print(f"La habitación {habitacion} no está reservada.")

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
        print("1. Agregar datos de registro") #? especificar que?
        print("2. Editar datos de registro")
        print("3. Eliminar cliente ")
        print("4. Realizar una reserva ")
        print("5. salir")
        
        opcion = input("Seleccione una opción: ")
        system ("cls")
        while True:
            if opcion == "1":
                registro()
                break
            if opcion=="2":
                editar()
                break
            if opcion=="3":
                eliminar()
                break
            while True:
                if opcion== "4":
                    mostrar_habitaciones()
                    registrar_reserva()
                    numero_habitacion=int(input("Ingrese el numero de habitación -> "))
                    noches=int(input("Ingrese el numero de noches -> "))
                    personas=int(input("Ingrese la cantidad de personas -> "))
                    hacer_reserva(numero_habitacion,noches,personas)
                    
                    
                    consultar_reserva()
                break
            if opcion=="5":
                print("Cerrando programa...")
                break
        break