import sqlite3
from flask import render_template, session, Flask
from . import hombres

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

@hombres.route('/hombres')
def hom():
    loggedIn, nom_user, noOfItems = getLoginDetails()
    return render_template("hombres.html", loggedIn=loggedIn, nom_user=nom_user, noOfItems=noOfItems)