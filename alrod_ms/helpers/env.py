from dotenv import load_dotenv
import os

load_dotenv()

"""CDiccionario de configuracion.
En esta sección se crea un diccionario con las variables de configuración
cargadas en el ambiente.
"""
ENV = os.getenv('ENV', 'dev')
APP_NAME = os.getenv('APP_NAME', 'App default')
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
