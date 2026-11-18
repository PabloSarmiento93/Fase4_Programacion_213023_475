# Registro de eventos y errores del sistema Software FJ

import logging

# Configuracion del archivo donde se guardaran los registros
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Registra las operaciones realizadas en el sistema
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registra los errores que se presenten
def registrar_error(mensaje):
    logging.error(mensaje)