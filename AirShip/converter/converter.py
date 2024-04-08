from .exceptions import InvalidConverterType, DisabledConverterType
from .utils import clean_converter_type
from .config import Config


def new_converter(converter_type=None):
    try:
        # ensure converter type is passed
        if converter_type is None:
            raise InvalidConverterType(f"converter type must be provided, detected NoneType")
        # clean the converter_type variable to reduce errors
        converter_type = clean_converter_type(converter_type)
        # look Up converter configuration
        selected = Config().getConverters().get(converter_type.upper(), None)
        # validate if converter_type is valid
        if selected is None:
            raise InvalidConverterType(f"unsupported converter type: {converter_type}")
        # validate if converter_type is enabled
        if selected["enabled"] is False:
            raise DisabledConverterType(f"converter type: {converter_type} is currently disabled or under development")
        # return correct converter class
        match selected.get(id,None).upper():
            case "CONTROLM":
                # return ControlMConverter() class
                return ControlMConverter()
            case _:
                # raise exception
                raise InvalidConverterType(f"unsupported converter type: {converter_type}")
        
    except (InvalidConverterType, DisabledConverterType) as e:
        return None


class AirShipConverter():
    def __init__(self, converter=None):
        pass

class ControlMConverter(AirShipConverter):
    def __init__(self):
        pass
