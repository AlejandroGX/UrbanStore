from flask import Blueprint

registrar = Blueprint('registrar', __name__, template_folder="templates", static_folder='static')
from . import register

registrado = Blueprint('registrado', __name__, template_folder="templates", static_folder='static')
from . import agregado

usuarios = Blueprint('usuarios', __name__, template_folder="templates", static_folder='static')
from . import usuario