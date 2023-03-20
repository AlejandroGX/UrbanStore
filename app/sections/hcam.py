import sqlite3
from flask import render_template, session
from . import hcamisetas
 
def getLoginDetails():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            nom_user = ''
            noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT id_user, nom_user FROM users WHERE email = ?", (session['email'], ))
            id_user, nom_user = cur.fetchone()
            cur.execute("SELECT count(id_cam) FROM kart WHERE id_user = ?", (id_user, ))
            noOfItems = cur.fetchone()[0]
    conn.close()
    return (loggedIn, nom_user, noOfItems)

@hcamisetas.route('/hombres/camisetas', methods= ["GET", "POST"])
def cam():
    loggedIn, nom_user, noOfItems = getLoginDetails()
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM camisetas")
    rows = cur.fetchall()
    return render_template("hcamisetas.html", rows = rows, loggedIn=loggedIn, nom_user=nom_user, noOfItems=noOfItems)