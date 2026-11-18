# Clase Reserva del sistema Software FJ

from cliente import Cliente
from servicios import Servicio
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)
from logs import registrar_evento, registrar_error


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        try:
            if not isinstance(cliente, Cliente):
                raise ReservaInvalidaError(
                    "La reserva debe tener un cliente valido."
                )

            if not isinstance(servicio, Servicio):
                raise ReservaInvalidaError(
                    "La reserva debe tener un servicio valido."
                )

            if (
                isinstance(duracion, bool)
                or not isinstance(duracion, (int, float))
                or duracion <= 0
            ):
                raise ReservaInvalidaError(
                    "La duracion debe ser mayor que cero."
                )

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"
            self.costo = 0

        except ReservaInvalidaError as error:
            registrar_error(f"Error al crear reserva: {error}")
            raise

        else:
            registrar_evento("Reserva creada correctamente.")

    # Confirma la reserva
    def confirmar(self):
        try:
            if self.estado != "Pendiente":
                raise OperacionNoPermitidaError(
                    "Solo se pueden confirmar reservas pendientes."
                )

            if not self.servicio.esta_disponible():
                raise OperacionNoPermitidaError(
                    "El servicio no esta disponible."
                )

            self.estado = "Confirmada"

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error al confirmar reserva: {error}")
            raise

        else:
            registrar_evento("Reserva confirmada correctamente.")

    # Cancela la reserva
    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise OperacionNoPermitidaError(
                    "La reserva ya esta cancelada."
                )

            if self.estado == "Procesada":
                raise OperacionNoPermitidaError(
                    "No se puede cancelar una reserva procesada."
                )

            self.estado = "Cancelada"

        except OperacionNoPermitidaError as error:
            registrar_error(f"Error al cancelar reserva: {error}")
            raise

        else:
            registrar_evento("Reserva cancelada correctamente.")

    # Procesa la reserva y calcula su costo
    def procesar(self, impuesto=0, descuento=0):
        try:
            if self.estado != "Confirmada":
                raise OperacionNoPermitidaError(
                    "Primero debe confirmar la reserva."
                )

            costo_calculado = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento
            )

            if costo_calculado < 0:
                raise OperacionNoPermitidaError(
                    "El costo calculado no puede ser negativo."
                )

        except Exception as error:
            registrar_error(f"Error al procesar reserva: {error}")
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.costo = costo_calculado
            self.estado = "Procesada"
            registrar_evento("Reserva procesada correctamente.")

        finally:
            registrar_evento(
                "Finalizo el intento de procesamiento de reserva."
            )

    # Muestra la informacion de la reserva
    def mostrar_reserva(self):
        datos_cliente = self.cliente.obtener_datos()

        return (
            f"Cliente: {datos_cliente['nombre']}\n"
            f"Servicio: {self.servicio.obtener_nombre()}\n"
            f"Duracion: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo: ${self.costo:,.2f}"
        )