import sqlite3
from flask import render_template, session
from . import mjeans

def getLoginDetails():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            nom_user = ''
            #noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT id_user, nom_user FROM users WHERE email = ?", (session['email'], ))
            id_user, nom_user = cur.fetchone()
            """cur.execute("SELECT count(productId) FROM kart WHERE userId = ?", (id_user, ))
            noOfItems = cur.fetchone()[0]"""
    conn.close()
    return (loggedIn, nom_user)

@mjeans.route('/mujeres/jeans')
def jeam():
    loggedIn, nom_user = getLoginDetails()
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM mpantalon")
    rows = cur.fetchall()
    return render_template("mjeans.html", rows=rows, loggedIn=loggedIn, nom_user=nom_user)