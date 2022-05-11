import logging
from logging.handlers import RotatingFileHandler
import os
# modulos personalizados
import helpers.env as env

"""Configuracion para la generacion del log.
En esta seccion se pueden configurar los valores generales para
escribir los logs de la aplicación
"""
LOGS_DIR='logs/'
os.makedirs(LOGS_DIR, exist_ok=True)
logging.basicConfig(
    handlers = [
        RotatingFileHandler(
            f'{LOGS_DIR}/server.log',
            maxBytes=50000000, backupCount=2
        ),
        logging.StreamHandler()
    ],
    level = env.LOGGING_LEVEL,
    format = f'%(levelname)s [%(asctime)s] [{env.APP_NAME}] [{env.ENV}] [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')


def log(name: str):
    """Esta función crea un objeto de tipo logging el cual permite
    registrar informacion en los archivos de logde la aplicación.

        Args:
            name: El nombre para agregar al rastreo del log.

        Returns:
            El objeto de tipo logging que permite escribir en el log.
    """
    logger = logging.getLogger(name)
    return logger
