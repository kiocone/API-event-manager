import types
from database import query
import bcrypt

from shared import utilities

salt = bcrypt.gensalt(10)


def get_events():
    resp = query(f"SELECT * from events;")
    return resp


def get_event_by_id(*args):
    response = query(f"SELECT * FROM events where id = ?;", *args)
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def delete_event(index):
    query(f"UPDATE events set 'deleted'=true WHERE id = {index};")
    return {
                "message": "Event deleted",
            }, 200


def create_event(payload):
    value_set = utilities.payload_to_valueset(payload)
    query_response = query(f"INSERT INTO events SET {value_set};")
    print(query_response)
    return {"message": "User created"}, 200


def update_event(p_id: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE events set {value_set} WHERE id = {p_id};")
    return {"message": "User updated"}, 200


