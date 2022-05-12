from flask_apscheduler import APScheduler
from app import app
from helpers.events import tanks_data_emit
import helpers.env as env

# programador de tareas
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(id='tanks-data-emit', func=tanks_data_emit, trigger='interval', seconds=env.TANK_READING_TIME)
