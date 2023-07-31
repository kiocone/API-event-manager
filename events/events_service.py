import types
from database import query
import bcrypt

from shared import utilities

salt = bcrypt.gensalt(10)


def get_events():
    resp = query(f"SELECT * from events;")
    return resp


def get_event_by_id(*args):
    response = query(f"SELECT * FROM users where id = ?;", *args)
    if types.NoneType == type(response):
        response = [False]
    return response[0]


def delete_event(index):
    query(f"DELETE from users WHERE id = {index};")
    return {
                "message": "User deleted",
            }, 200


def create_event(payload):
    value_set = utilities.payload_to_valueset(payload)
    query_response = query(f"INSERT INTO events SET {value_set};")
    print(query_response)
    return {"message": "User created"}, 200


def update_event(p_id: int, payload):
    value_set = utilities.payload_to_valueset(payload)
    query(f"UPDATE users set {value_set} WHERE id = {p_id};")
    return {"message": "User updated"}, 200


def update_password(index: int, password: str, new_password: str):
    hashed_password = query(f"SELECT password FROM users where id = ?;", index)
    matched = bcrypt.checkpw(password, hashed_password[0]['password'])
    if matched:
        new_password = bcrypt.hashpw(new_password, salt)
        query(f"UPDATE users set password='{new_password}' WHERE id = {index};")
    return matched


def signin(username, password):
    # TODO: JWT Implementation
    q_response = query(f"SELECT username, password FROM users WHERE username='{username}'")
    return q_response[0]['username'] == username and bcrypt.checkpw(password, q_response[0]['password'])
