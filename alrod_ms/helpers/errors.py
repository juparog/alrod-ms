from app import app
from flask import json, make_response
from werkzeug.exceptions import HTTPException
import traceback
# modulos personalizados
from helpers.logger import log

# configurando el resgistrador de logs
logger = log(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    logger.debug('app.errorhandler helper')
    trace_error = traceback.format_exc()
    logger.error(trace_error)
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    response = make_response()
    response.data = json.dumps({
            "code": 500,
            "name": type(e).__name__,
            "description": trace_error,
        })
    response.content_type = "application/json"
    return response
