# Programa principal del sistema Software FJ

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import SistemaError
from logs import registrar_evento, registrar_error


# Lista para almacenar los clientes, servicios y reservas
clientes = []
servicios = []
reservas = []


# Registra un cliente
def registrar_cliente(nombre, documento, telefono, correo):
    try:
        cliente = Cliente(nombre, documento, telefono, correo)
        clientes.append(cliente)
        print("Cliente registrado correctamente.")

    except SistemaError as error:
        print(f"No se pudo registrar el cliente: {error}")


# Registra un servicio
def registrar_servicio(servicio):
    try:
        servicios.append(servicio)
        print(f"Servicio registrado: {servicio.describir()}")

    except SistemaError as error:
        registrar_error(f"Error al registrar servicio: {error}")
        print(f"No se pudo registrar el servicio: {error}")


# Crea una reserva
def crear_reserva(cliente, servicio, duracion):
    try:
        reserva = Reserva(cliente, servicio, duracion)
        reservas.append(reserva)
        print("Reserva creada correctamente.")
        return reserva

    except SistemaError as error:
        print(f"No se pudo crear la reserva: {error}")
        return None


# Pruebas del sistema
def ejecutar_pruebas():

    print("\n======================================")
    print(" SISTEMA SOFTWARE FJ")
    print(" Gestion de clientes y reservas")
    print("======================================\n")

    # Operacion 1: registrar un cliente valido
    print("OPERACION 1")
    registrar_cliente(
        "Carlos Ramirez", "12345678", "3101234567",
        "carlos@gmail.com"
    )

    # Operacion 2: registrar otro cliente valido
    print("\nOPERACION 2")
    registrar_cliente(
        "Laura Gomez", "87654321", "3119876543",
        "laura@gmail.com"
    )

    # Operacion 3: intentar registrar un cliente invalido
    print("\nOPERACION 3")
    registrar_cliente(
        "", "123", "123", "correoincorrecto"
    )

    # Operacion 4: crear un servicio de sala
    print("\nOPERACION 4")
    sala = ReservaSala(
        "Sala de reuniones", 50000, 10
    )
    registrar_servicio(sala)

    # Operacion 5: crear un servicio de alquiler de equipos
    print("\nOPERACION 5")
    equipo = AlquilerEquipo(
        "Computador portatil", 30000, "Computador"
    )
    registrar_servicio(equipo)

    # Operacion 6: crear un servicio de asesoria
    print("\nOPERACION 6")
    asesoria = AsesoriaEspecializada(
        "Asesoria de software", 80000, "Desarrollo de software"
    )
    registrar_servicio(asesoria)

    # Operacion 7: intentar crear un servicio con tarifa incorrecta
    print("\nOPERACION 7")
    try:
        servicio_invalido = ReservaSala(
            "Sala invalida", -10000, 5
        )
        registrar_servicio(servicio_invalido)

    except SistemaError as error:
        registrar_error(f"Servicio invalido: {error}")
        print(f"Error controlado: {error}")

    # Pruebas adicionales de validacion de servicios

    print("\nPRUEBA DE SALA CON CAPACIDAD INVALIDA")
    try:
        ReservaSala("Sala de prueba", 50000, 0)
    except SistemaError as error:
        print(f"Error controlado: {error}")

    print("\nPRUEBA DE EQUIPO SIN TIPO")
    try:
        AlquilerEquipo("Equipo de prueba", 30000, "")
    except SistemaError as error:
        print(f"Error controlado: {error}")

    print("\nPRUEBA DE ASESORIA SIN ESPECIALIDAD")
    try:
        AsesoriaEspecializada("Asesoria de prueba", 80000, "")
    except SistemaError as error:
        print(f"Error controlado: {error}") 

    # Operacion 8: crear y confirmar una reserva
    print("\nOPERACION 8")
    reserva1 = crear_reserva(
        clientes[0], sala, 2
    )

    if reserva1:
       try:
        reserva1.confirmar()
        reserva1.procesar(impuesto=19, descuento=5)
        print(reserva1.mostrar_reserva())

       except SistemaError as error:
        registrar_error(f"Error en la operacion 8: {error}")
        print(f"Error controlado: {error}")

    # Operacion 9: intentar crear una reserva con duracion incorrecta
    print("\nOPERACION 9")
    crear_reserva(
        clientes[1], equipo, -2
    )
    
    print("\nOPERACION 10")
    reserva2 = crear_reserva(
        clientes[1], asesoria, 1
    )
    
    if reserva2:
       try:
        reserva2.cancelar()
        print(reserva2.mostrar_reserva())

       except SistemaError as error:
        registrar_error(f"Error en la operacion 10: {error}")
        print(f"Error controlado: {error}")
        
    # Prueba adicional: diferentes formas de calcular el costo
    print("\nPRUEBA DE PARAMETROS OPCIONALES")

    print("Calculo basico:")
    print(sala.calcular_costo(2))

    print("Calculo con impuesto:")
    print(sala.calcular_costo(2, 19))

    print("Calculo con impuesto y descuento:")
    print(sala.calcular_costo(2, 19, 5))

    print("\n======================================")
    print(" RESUMEN DEL SISTEMA")
    print("======================================")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")
    print("\nProceso de pruebas finalizado.")

    registrar_evento("Finalizaron las pruebas del sistema.")


# Ejecuta el programa
if __name__ == "__main__":
    ejecutar_pruebas()