# modulos de pip
from flask_socketio import emit
from flask import request
import traceback
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

@socketio.on_error_default
def default_error_handler(e):
    logger.debug('ws:on_error_default helper')
    logger.debug(request.event["message"])
    logger.debug(request.event["args"])
    logger.error(e, traceback.format_exc())
