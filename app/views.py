from flask import Blueprint, json

from . import db
from .models import PlanTask


bp_main = Blueprint('bp_main', __name__)

# TODO: MVC-C
@bp_main.route('/example', methods=['GET', 'POST'])
def uppercase():
    case = {'a': 'A'}
    return json.jsonify(success=True, data=case)
