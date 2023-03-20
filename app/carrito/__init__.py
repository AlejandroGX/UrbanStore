from flask import Blueprint

carrito = Blueprint('carrito', __name__, template_folder="templates", static_folder='static')
from . import cart