# Excepciones personalizadas del sistema Software FJ

# Error general del sistema
class SistemaError(Exception):
    pass


# Error cuando los datos de un cliente no son validos
class ClienteInvalidoError(SistemaError):
    pass


# Error cuando un servicio no esta disponible
class ServicioNoDisponibleError(SistemaError):
    pass


# Error cuando una reserva tiene datos incorrectos
class ReservaInvalidaError(SistemaError):
    pass


# Error cuando se intenta realizar una operacion no permitida
class OperacionNoPermitidaError(SistemaError):
    pass