from app.utils.exceptions import ValidationError
from app.core.parsers.controlm.controlm_parser import ControlMParser


def create_analyses():
    cmp = ControlMParser(
        xml_path="",
    )
    
    cmp.analyze()
    
   
    return


def get_analyses_by_conversion_id(conversion_id=None): 
    # TODO: Implement 
    raise NotImplementedError
    if conversion_id is None: 
        raise ValidationError("conversion id required")
    return


def get_analyses_by_id(analyses_id=None): 
    # TODO: Implement 
    raise NotImplementedError
    if analyses_id is None: 
        raise ValidationError("analyses id required")
    return


def delete_analyses_by_id(analyses_id=None): 
    # TODO: Implement 
    raise NotImplementedError
    if analyses_id is None: 
        raise ValidationError("analyses id required")
    return