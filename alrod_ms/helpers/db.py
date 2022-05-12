import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from helpers.logger import log

# definicion de variables globales
logger = log(__name__)

def firestoreClient():
    """Esta función crea un objeto de tipo firestore client el cual
    permite conectarce a Firebase y realizar operaciones en Firestore.

        Returns:
            El objeto de tipo firestore client para realizar operaciones en Firebase-Firestore.
    """
    logger.debug('firestoreClient helper')
    cred = credentials.Certificate("./credentials.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()
