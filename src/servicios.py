# Clases de servicios del sistema Software FJ

from abc import ABC, abstractmethod
from excepciones import (
    ServicioNoDisponibleError,
    OperacionNoPermitidaError
)
from logs import registrar_evento, registrar_error


# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, tarifa, disponible=True):
        try:
            if not isinstance(nombre, str) or not nombre.strip():
                raise OperacionNoPermitidaError(
                    "El nombre del servicio es obligatorio."
                )

            if isinstance(tarifa, bool) or not isinstance(tarifa, (int, float)) or tarifa <= 0:
                raise OperacionNoPermitidaError(
                    "La tarifa debe ser un valor mayor que cero."
                )

            if not isinstance(disponible, bool):
                raise OperacionNoPermitidaError(
                    "La disponibilidad debe ser verdadera o falsa."
                )

            self.__nombre = nombre
            self.__tarifa = tarifa
            self.__disponible = disponible

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error en servicio: {error}")
            raise
    
    # Permite consultar los datos del servicio
    def obtener_nombre(self):
        return self.__nombre

    def obtener_tarifa(self):
        return self.__tarifa

    def esta_disponible(self):
        return self.__disponible

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    # Calcula el costo del servicio con diferentes opciones
    def calcular_total(self, duracion, impuesto=0, descuento=0):

        try:
            if not self.__disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio {self.__nombre} no esta disponible."
                )

            if (
                isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
                or duracion <= 0
            ):
                raise OperacionNoPermitidaError(
                    "La duracion debe ser mayor que cero."
                )

            if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
                raise OperacionNoPermitidaError(
                    "El impuesto debe estar entre 0 y 100."
                )

            if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
                raise OperacionNoPermitidaError(
                    "El descuento debe estar entre 0 y 100."
                )

            subtotal = self.__tarifa * duracion
            valor_impuesto = subtotal * (impuesto / 100)
            valor_descuento = subtotal * (descuento / 100)

            total = subtotal + valor_impuesto - valor_descuento

        except (ServicioNoDisponibleError, OperacionNoPermitidaError) as error:
            registrar_error(f"Error al calcular costo: {error}")
            raise

        else:
            registrar_evento(
                f"Costo calculado para {self.__nombre}: {total}"
            )
            return total


# Servicio para reservar salas
class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa, capacidad, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        self.capacidad = capacidad
        self.validar_parametros()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_total(duracion, impuesto, descuento)

    def describir(self):
        return (
            f"Sala: {self.obtener_nombre()} - "
            f"Capacidad: {self.capacidad} personas"
        )

    def validar_parametros(self):
        try:
            if (
                isinstance(self.capacidad, bool)
                or not isinstance(self.capacidad, int)
                or self.capacidad <= 0
            ):
                raise OperacionNoPermitidaError(
                    "La capacidad de la sala debe ser mayor que cero."
                )

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error en sala: {error}")
            raise


# Servicio para alquilar equipos
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, tarifa, tipo_equipo, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        self.tipo_equipo = tipo_equipo
        self.validar_parametros()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_total(duracion, impuesto, descuento)

    def describir(self):
        return (
            f"Equipo: {self.obtener_nombre()} - "
            f"Tipo: {self.tipo_equipo}"
        )

    def validar_parametros(self):
        try:
            if not isinstance(self.tipo_equipo, str) or not self.tipo_equipo.strip():
                raise OperacionNoPermitidaError(
                    "Debe indicar el tipo de equipo."
                )

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error en equipo: {error}")
            raise


# Servicio de asesorias especializadas
class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, tarifa, especialidad, disponible=True):
        super().__init__(nombre, tarifa, disponible)
        self.especialidad = especialidad
        self.validar_parametros()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        return self.calcular_total(duracion, impuesto, descuento)

    def describir(self):
        return (
            f"Asesoria: {self.obtener_nombre()} - "
            f"Especialidad: {self.especialidad}"
        )

    def validar_parametros(self):
        try:
            if not isinstance(self.especialidad, str) or not self.especialidad.strip():
                raise OperacionNoPermitidaError(
                    "Debe indicar la especialidad de la asesoria."
                )

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error en asesoria: {error}")
            raise