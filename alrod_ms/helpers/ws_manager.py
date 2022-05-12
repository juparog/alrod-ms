# modulos de pip
from flask_socketio import emit
# modulos personalizados
from app import socketio
from helpers.logger import log

# configurando el resgistrador de logs
logger = log(__name__)

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
