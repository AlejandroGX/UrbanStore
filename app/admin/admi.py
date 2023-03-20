import sqlite3
from flask import render_template
from . import administrador

@administrador.route('/administracion', methods= ["GET", "POST"])
def adm():
    return render_template("admin.html")

@administrador.route('/administracion/clientes', methods= ["GET", "POST"])
def cli():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    cur.execute("SELECT * FROM kart")
    rows = cur.fetchall();
    return render_template("list_clientes.html", rows=rows)