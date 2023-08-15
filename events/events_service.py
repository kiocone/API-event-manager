import types
from database import query

from shared import utilities


def get_events(managed=None):
    query_str = f"SELECT * from events WHERE deleted=false;"
    if managed:
        query_str = query_str[0:-1] + " AND managed=true;"
    resp = query(query_str)
    return resp


def get_event_by_id(*args):
    response = query(f"SELECT * FROM events where deleted=false AND id = ?;", *args)
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
    return {"message": "User created"}, 201


def update_event(p_id: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE events set {value_set} WHERE deleted=false AND id = {p_id};")
    return {"message": "User updated"}, 200


