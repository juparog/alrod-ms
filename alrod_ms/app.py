# modulos de pip
from flask import Flask
from flask_socketio import SocketIO
# modulos personalizados
from helpers.db import firestore_client
import helpers.env as env
from helpers.logger import log
from blueprints.home.views import home
from blueprints.ws.views import ws

# configurando el resgistrador de logs
logger = log(__name__)

# crear y configurar la app http
logger.debug('creating app...')
app = Flask(__name__, static_folder = './blueprints/static')
app.register_blueprint(home)
app.register_blueprint(ws)

# crear y configurar la conexxion websocket
logger.debug('creating websocket...')
socketio = SocketIO(app, logger=True, engineio_logger=True)

# crear la conexon con la base de datos
logger.debug('creating db...')
db = firestore_client()
