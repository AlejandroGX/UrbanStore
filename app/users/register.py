from flask import render_template, request, url_for, redirect
from . import registrar
 
@registrar.route('/registrarse')
def reg():
    return render_template("registrar.html")
