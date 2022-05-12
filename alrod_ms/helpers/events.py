import random
import sys
from app import socketio
import helpers.env as env
from helpers.logger import log

# configurando el resgistrador de logs
logger = log(__name__)

# capturar la interrupcion por teclado
def keyboard_signal_handler(signal, frame):
    logger.debug('keyboard_signal_handler event')
    logger.debug('You pressed Ctrl+C!')
    logger.debug('Stopping the server...')
    socketio.stop()
    sys.exit(0)


def read_tanks():
    reading = random.randint(350,500)
    return reading

def tanks_data_emit():
    reading = random.randint(350,500)
    socketio.emit('tanks-data-event', {
        'tanks': {
            f'{env.TANK_ID}': {
                'value': reading
            }
        }
    })
