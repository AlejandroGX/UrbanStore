from flask import render_template, request, url_for, redirect
from . import usuarios
 
@usuarios.route('/usuario')
def usu():
    return render_template("vistausu.html")