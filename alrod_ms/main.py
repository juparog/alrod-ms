import signal
# modulos personalizados
from app import app, socketio
from helpers.ws_manager import *
from helpers.scheduler import *
from helpers.errors import *
import helpers.env as env
from helpers.events import keyboard_signal_handler
from helpers.logger import log

# configurando el resgistrador de logs
logger = log(__name__)

def test_job():
    print('I am working...')

# funcion principal
def main():
    logger.debug('main Function')
    socketio.run(app, port = env.PORT)

if __name__ == "__main__":
    logger.info(f'Initializing {env.APP_NAME}')
    try:
        signal.signal(signal.SIGINT, keyboard_signal_handler)
        main()
    except Exception as ex:
        logger.error(ex)
