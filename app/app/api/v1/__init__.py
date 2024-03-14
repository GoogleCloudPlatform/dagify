from flask import Blueprint
from app.api import bp as api_bp

bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(bp, url_prefix='/v1')

#from app.api.v1 import analyses_findings
#from app.api.v1 import analyses
#from app.api.v1 import conversions
#from app.api.v1 import core