from flask import Blueprint

oneerror = Blueprint('oneerror', __name__, template_folder="templates", static_folder='static')
from . import onerro

seconderror = Blueprint('seconderror', __name__, template_folder="templates", static_folder='static')
from . import seconderro