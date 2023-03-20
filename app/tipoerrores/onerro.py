from flask import render_template, request, url_for, redirect
from . import oneerror
 
@oneerror.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada"), 404