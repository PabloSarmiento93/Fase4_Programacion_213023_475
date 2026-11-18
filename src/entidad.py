# Clase abstracta general del sistema Software FJ

from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError(
                "La entidad debe tener un identificador valido."
            )

        self.__identificador = identificador

    # Permite consultar el identificador
    def obtener_identificador(self):
        return self.__identificador

    # Cada entidad debe mostrar su informacion
    @abstractmethod
    def mostrar_informacion(self):
        pass