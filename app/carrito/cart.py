import sqlite3
from flask import render_template, request, url_for, redirect
from . import carrito
 
@carrito.route('/login', methods= ["GET", "POST"])
def car():
    return render_template("carrito.html")