import sqlite3
from flask import Flask, session, redirect, flash, render_template, url_for, request, abort

from sections import hombres
from sections import mujeres
from sections import hchaquetas
from sections import hcamisetas
from sections import hjeans
from sections import mbuzos
from sections import mblusas
from sections import mjeans
from login import login
from admin import administrador
from admin import prendas
from admin import paginacion
from users import registrar
from users import registrado
from users import usuarios
from tipoerrores import seconderror

app = Flask(__name__)

app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

app.register_blueprint(hombres)
app.register_blueprint(mujeres)
app.register_blueprint(hchaquetas)
app.register_blueprint(hcamisetas)
app.register_blueprint(hjeans)
app.register_blueprint(mbuzos)
app.register_blueprint(mblusas)
app.register_blueprint(mjeans)
app.register_blueprint(login)
app.register_blueprint(administrador)
app.register_blueprint(prendas)
app.register_blueprint(registrar)
app.register_blueprint(registrado)
app.register_blueprint(usuarios)
app.register_blueprint(paginacion)
app.register_blueprint(seconderror)

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

@app.route('/')
def ini():
    loggedIn, nom_user, noOfItems= getLoginDetails()
    return render_template("index.html", loggedIn=loggedIn, nom_user=nom_user, noOfItems=noOfItems)

@app.route("/propietarios")
def propi():
    return render_template("propietarios.html")

@app.route("/contactanos")
def contac():
    return render_template("contactos.html")

@app.route("/enviar")
def envia():
    abort(503)
    
@app.route("/pagar")
def paga():
    abort(501)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('ini'))

@app.route("/cart")
def cart():
    if 'email' not in session:
        return redirect(url_for('login.loginForm'))
    loggedIn, nom_user, noOfItems = getLoginDetails()
    email = session['email']
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT id_user FROM users WHERE email = ?", (email, ))
        id_user= cur.fetchone()[0]
        cur.execute("SELECT camisetas.id_cam, camisetas.nom_cam, camisetas.precio_cam, camisetas.url_cam, kart.quantity FROM camisetas, kart WHERE camisetas.id_cam = kart.id_cam AND kart.id_user= ?", (id_user, ))
        products = cur.fetchall()
    totalPrice = 0
    for row in products:
        totalPrice += row[2] * row[4]
    return render_template("cart.html", products=products, totalPrice=totalPrice, loggedIn=loggedIn, nom_user=nom_user, noOfItems=noOfItems)

@app.route("/addToCart")
def addToCart():
    if 'email' not in session:
        return redirect(url_for('login.loginForm'))
    else:
        id_producto = request.args.get('id_cam')
        id_cam = int(id_producto)
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT id_user FROM users WHERE email = ?", (session['email'], ))
            id_user = cur.fetchone()[0]
            # Buscar si el producto ya está en el carrito del usuario
            cur.execute("SELECT quantity FROM kart WHERE id_user = ? AND id_cam = ?", (id_user, id_cam))
            result = cur.fetchone()
            if result:
                # Si el producto ya está en el carrito, aumentar la cantidad en 1
                quantity = result[0] + 1
                cur.execute("UPDATE kart SET quantity = ? WHERE id_user = ? AND id_cam = ?", (quantity, id_user, id_cam))
            else:
                # Si el producto no está en el carrito, agregarlo con cantidad 1
                cur.execute("INSERT INTO kart (id_user, id_cam, quantity) VALUES (?, ?, ?)", (id_user, id_cam, 1))
                
            msg = "Added successfully"
            # Reducir el stock del producto en la base de datos
            #cur.execute('''UPDATE products SET stock = stock - 1 WHERE productId = ?''', (productId,))                
            conn.commit()                
            
        conn.close()
        return redirect(url_for('ini'))

@app.route("/removeFromCart")
def removeFromCart():
    if 'email' not in session:
        return redirect(url_for('login.loginForm'))
    email = session['email']
    proId = request.args.get('id_cam')
    id_cam = int(proId)
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT id_user FROM users WHERE email = ?", (email, ))
        id_user = cur.fetchone()[0]
        try:
            # Buscar si el producto ya está en el carrito del usuario
            cur.execute("SELECT quantity FROM kart WHERE id_user = ? AND id_cam = ? AND quantity > 0", (id_user, id_cam))
            result = cur.fetchone()
            if result:                  
                cur.execute("UPDATE kart SET quantity = quantity - 1 WHERE id_user = ? AND id_cam = ? AND quantity > 0", (id_user, id_cam))
                conn.commit()
                msg = "removed successfully"              
            else:
                 cur.execute("DELETE FROM kart WHERE id_user = ? AND id_cam = ?", (id_user, id_cam))
        except:
            conn.rollback()
            msg = "error occured"
    conn.close()
    return redirect(url_for('cart'))

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada"), 404

@app.errorhandler(401)
def unauthorized(error):
	return render_template("error401.html",error="No autorizado"), 401

@app.errorhandler(501)
def not_implemented(error):
	return render_template("error501.html",error="No implementado"), 501

@app.errorhandler(503)
def service_unavailable(error):
	return render_template("error503.html",error="Servicio no disponible"), 503

if __name__ == '__main__':
    app.run(debug=True, port=8000)