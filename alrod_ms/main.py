# modulos de pip
from flask import Flask
from flask_socketio import SocketIO, emit
# modulos personalizados
from helpers.db import firestoreClient
import helpers.env as env
from helpers.logger import log
from blueprints.home.views import home
from blueprints.ws.views import ws

# configurando el resgistrador de logs
logger = log(__name__)
logger.info(f'Iniciando {env.APP_NAME}')

# crear y configurar la app http
app = Flask(__name__, static_folder = './blueprints/static')
app.register_blueprint(home)
app.register_blueprint(ws)

# crear y configurar la conexxion websocket
socketio = SocketIO(app)
@socketio.on('input-data-event')
def test_message(message):
    logger.debug('ws:input-data-event helper')
    logger.debug(message)
    emit('output-data-event', {'data': message['data']})

@socketio.on('broadcast-event')
def test_message(message):
    logger.debug('ws:broadcast-event helper')
    logger.debug(message)
    emit('output-data-event', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    logger.debug('ws:connect helper')
    emit('output-data-event', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    logger.debug('ws:disconnect helper')
    logger.debug('Client disconnected')

# crear la conexon con la base de datos
db = firestoreClient()
# funcion para crear el websocket

# funcion principal
def main():
    logger.debug('main Function')
    socketio.run(app, port = env.PORT)

if __name__ == "__main__":
    main()
