import sqlite3
from flask import render_template
from . import prendas

@prendas.route('/administracion/prendas', methods= ["GET", "POST"])
def pre():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    cur.execute("select * from chaquetas")  
    rows1 = cur.fetchall(); 
    cur.execute("select * from camisetas")  
    rows2 = cur.fetchall();
    cur.execute("select * from hpantalon")  
    rows3 = cur.fetchall();
    return render_template("list_prendas.html",rows1 = rows1, rows2 = rows2, rows3 = rows3)