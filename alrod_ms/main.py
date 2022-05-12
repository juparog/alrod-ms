# modulos personalizados
from app import app, socketio
from helpers.ws_manager import *
from helpers.errors import *
import helpers.env as env
from helpers.logger import log

# configurando el resgistrador de logs
logger = log(__name__)

# funcion principal
def main():
    logger.debug('main Function')
    socketio.run(app, port = env.PORT)

if __name__ == "__main__":
    logger.info(f'Initializing {env.APP_NAME}')
    try:
        main()
    except Exception as ex:
        logger.error(ex)
