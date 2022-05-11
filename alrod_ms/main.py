# modulos personalizados
from helpers.db import firestoreClient
import helpers.env as env
from helpers.logger import log

# definicion de variables globales
logger = log(__name__)
logger.info(f'Iniciando {env.APP_NAME}')
db = firestoreClient()
doc_ref = db.collection('users').document()
