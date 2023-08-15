import os
import datetime
from flask import Flask
from markupsafe import escape
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

# Controllers modules
from events import events_controller


# event loger
def update_log(datos):
    today = str(datetime.datetime.now()).split()[0]
    try:
        with open(f'event_log/{today}.txt', 'a') as archivo:
            archivo.write(f'{datetime.datetime.now()} - {datos}\n')
    except FileNotFoundError:
        os.mkdir('event_log')
        with open(f'./event_log/{today}.txt', 'a') as archivo:
            archivo.write(f'{datetime.datetime.now()} - {datos}\n')


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={ 
        'app_name': "Events manager app"
    }
)

app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(events_controller.events_bp)


@app.route('/<parametro>')
def panel_param(parametro):
    parametro = escape(parametro)
    update_log(parametro)
    return f"<h1>404: {parametro} no se encuentra</h1><p>La ruta [/{parametro}] no esta definida</p>", 404

