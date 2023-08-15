import datetime


def payload_to_valueset(payload):
    value_set = ""
    for value in dict(payload).keys():
        if key_value_valid(value, dict(payload)[value]):
            if str(dict(payload)[value]).lower() == "true" or str(dict(payload)[value]).lower() == "false":
                value_set += f"{value}={str(dict(payload)[value]).lower()},"
            else:
                value_set += f"{value}='{dict(payload)[value]}',"
    return value_set[0:-1]


def key_value_valid(key, value):
    """
    :param key: str | bool
    :param value: str
    :return: bool
    Verifies if key is True or not empty string and has value
    """
    if type(key) == bool:
        return bool(key) and str(value).strip() != ""
    else:
        return str(key).strip() != "" and str(value).strip() != ""

