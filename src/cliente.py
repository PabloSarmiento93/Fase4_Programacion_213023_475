# Clase Cliente del sistema Software FJ

from entidad import Entidad
from excepciones import ClienteInvalidoError
from logs import registrar_evento, registrar_error


class Cliente(Entidad):

    def __init__(self, nombre, documento, telefono, correo):
        try:
            self.__nombre = nombre
            self.__documento = documento
            self.__telefono = telefono
            self.__correo = correo

            self.validar_datos()
            super().__init__(self.__documento)

            registrar_evento(
                f"Cliente registrado: {self.__nombre}"
            )

        except ClienteInvalidoError as error:
            registrar_error(f"Error al registrar cliente: {error}")
            raise

    # Valida los datos del cliente
    def validar_datos(self):

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ClienteInvalidoError(
                "El nombre del cliente es obligatorio."
            )

        if not isinstance(self.__documento, str):
            raise ClienteInvalidoError(
                "El documento debe ser texto."
            )

        if not self.__documento.isdigit() or len(self.__documento) < 6:
            raise ClienteInvalidoError(
                "El documento debe tener al menos 6 digitos."
            )

        if not isinstance(self.__telefono, str):
            raise ClienteInvalidoError(
                "El telefono debe ser texto."
            )

        if not self.__telefono.isdigit() or len(self.__telefono) < 7:
            raise ClienteInvalidoError(
                "El telefono debe tener al menos 7 digitos."
            )

        if not isinstance(self.__correo, str):
            raise ClienteInvalidoError(
                "El correo debe ser texto."
            )

        if (
            "@" not in self.__correo
            or "." not in self.__correo.split("@")[-1]
            or " " in self.__correo
        ):
            raise ClienteInvalidoError(
                "El correo electronico no es valido."
            )

    # Permite consultar los datos del cliente
    def obtener_datos(self):
        return {
            "nombre": self.__nombre,
            "documento": self.__documento,
            "telefono": self.__telefono,
            "correo": self.__correo
        }

    # Muestra la informacion del cliente
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Telefono: {self.__telefono}\n"
            f"Correo: {self.__correo}"
        )