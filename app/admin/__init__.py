from flask import Blueprint

administrador = Blueprint('administrador', __name__, template_folder="templates", static_folder='static')
from . import admi

prendas = Blueprint('prendas', __name__, template_folder="templates", static_folder='static')
from . import prenda

paginacion = Blueprint('paginacion', __name__, template_folder="templates", static_folder='static')
from . import paginaci