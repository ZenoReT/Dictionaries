"""Module with subsidiary functions"""


def parse_int(element):
    """The number from string, if it can parse, else None"""
    try:
        return int(element)
    except TypeError:
        return None


def check_type(elements_type):
    """Checks the type of future dictionary elements."""
    """If this type does not exist in the python returns None"""
    if elements_type == "str":
        return (True, str)
    elif elements_type == "int":
        return (True, int)
    elif elements_type == "float":
        return (True, float)
    return (False, "incorrect type")


def try_lead_to(element, elements_type):
    if elements_type is str:
        try:
            return str(element)
        except TypeError:
            return None
    elif elements_type is int:
        try:
            return int(element)
        except TypeError:
            return None
    elif elements_type is float:
        try:
            return float(element)
        except TypeError:
            return None
