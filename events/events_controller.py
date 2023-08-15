from flask import Blueprint, request
from events.events_service import *

events_bp = Blueprint('events', __name__)


@events_bp.get('/v1/events')
def all_events():
    managed = request.args.get('managed', None, str)
    response = get_events(managed)
    if response is None:
        response = {
                "message": "No events found",
            }, 404
    return response


@events_bp.get('/v1/events/<int:index>')
def events_by_id(index):
    response = get_event_by_id(index)
    if response is None or response is False:
        response = {
                "message": "Event not found",
            }, 404
    return response


@events_bp.post('/v1/events')
def new_event():
    response = ""
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = create_event(request.json)
    else:
        print('Content-Type not supported!')
        response = 'Content-Type not supported!'
    return response


@events_bp.put('/v1/events/<int:index>')
def upd_event(index):
    response = ""
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = update_event(index, request.json)
    else:
        print('Content-Type not supported!')
    return response


@events_bp.delete('/v1/events/<int:index>')
def del_event(index):
    respuesta = delete_event(index)
    return respuesta


