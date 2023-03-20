from flask import render_template, request, url_for, redirect
from . import seconderror
 
@seconderror.errorhandler(401)
def unauthorized(error):
	return render_template("error401.html",error="No autorizado"), 401