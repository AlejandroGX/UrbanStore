from flask import Blueprint

hombres = Blueprint('hombres', __name__, template_folder="templates", static_folder='static')
from . import hombre

mujeres = Blueprint('mujeres', __name__, template_folder="templates", static_folder='static')
from . import mujer

hchaquetas = Blueprint('hchaquetas', __name__, template_folder="templates", static_folder='static')
from . import hcha

hcamisetas = Blueprint('hcamisetas', __name__, template_folder="templates", static_folder='static')
from . import hcam

hjeans = Blueprint('hjeans', __name__, template_folder="templates", static_folder='static')
from . import hjea

mbuzos = Blueprint('mbuzos', __name__, template_folder="templates", static_folder='static')
from . import mbuz

mblusas = Blueprint('mblusas', __name__, template_folder="templates", static_folder='static')
from . import mblu

mjeans = Blueprint('mjeans', __name__, template_folder="templates", static_folder='static')
from . import mjea