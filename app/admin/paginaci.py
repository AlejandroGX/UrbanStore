import sqlite3
from flask import render_template
from . import paginacion

@paginacion.route('/prendas/<num_page>', methods= ["GET", "POST"])
def pag(num_page):
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()
    
    if num_page == '1':
        cur.execute("SELECT * FROM chaquetas")
        rows1 = cur.fetchall();
        return render_template('list_prendas.html', rows1 = rows1)
    elif num_page == '2':
        cur.execute("SELECT * FROM camisetas")
        rows2 = cur.fetchall();
        return render_template('list_prendas.html', rows2 = rows2)
    elif num_page == '3':
        cur.execute("SELECT * FROM hpantalon")
        rows3 = cur.fetchall();
        return render_template('list_prendas.html', rows3 = rows3)
    elif num_page == '4':
        cur.execute("SELECT * FROM buzos")
        rows4 = cur.fetchall();
        return render_template('list_prendas.html', rows4 = rows4)
    elif num_page == '5':
        cur.execute("SELECT * FROM blusas")
        rows5 = cur.fetchall();
        return render_template('list_prendas.html', rows5 = rows5)
    elif num_page == '6':
        cur.execute("SELECT * FROM mpantalon")
        rows6 = cur.fetchall();
        return render_template('list_prendas.html', rows6 = rows6)
    