from flask import Blueprint, request
from events.events_service import *

events_bp = Blueprint('events', __name__)


@events_bp.get('/events')
def all_events():
    """
    List all events
    ---
    description: hola mundo
    responses:
        '200':
            schema:
                type: array
                items:
                    event:
                        properties:
                            event_date:
                                type: string
                                description: date for event
                            description:
                                type: string
                                description: name for event
                            type:
                                type: string
                                description: string '1', '2' or '3'
                            viewed:
                                type: boolean
                                description: wether the event has been reviewd or not
                            managed:
                                type: boolean
                                description: wether the event require management or not
                            deleted:
                                type: boolean
                                description: wether the event is soft deleted or not
    """
    response = get_events()
    if response is None:
        response = {
                "message": "No events found",
            }, 404
    return response


@events_bp.get('/events/<int:index>')
def events_by_id(index):
    response = get_event_by_id(index)
    if response is None or response is False:
        response = {
                "message": "Event not found",
            }, 404
    return response


@events_bp.post('/events')
def new_event():
    response = ""
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = create_event(request.json)
    else:
        print('Content-Type not supported!')
    return response


@events_bp.put('/events/<int:index>')
def upd_event(index):
    response = ""
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        response = update_event(index, request.json)
    else:
        print('Content-Type not supported!')
    return response


@events_bp.delete('/events/<int:index>')
def del_event(index):
    respuesta = delete_event(index)
    return respuesta


