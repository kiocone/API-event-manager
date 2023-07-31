import os
import datetime
from flask import Flask, jsonify
from flask_swagger import swagger
from markupsafe import escape
from flask_cors import CORS

# Controllers modules
from events import events_controller
# from pacientes import pacientes_controller

# event loger
today = str(datetime.datetime.now()).split()[0]


def update_log(datos):
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


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Event manager API"
    return jsonify(swag)


app.register_blueprint(events_controller.events_bp)


@app.get('/<parametro>')
def panel_param(parametro):
    update_log(parametro)
    return f"<h1>{parametro}</h1><p>La ruta [/{parametro}] no esta definida</p>"


@app.get('/')
def panel():
    return "<h1>panel</h1>"
