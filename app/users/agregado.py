import sqlite3, hashlib
from flask import render_template, request, url_for, redirect
from . import registrado
 
@registrado.route('/registrado', methods= ["GET", "POST"])
def agre():
    if request.method == 'POST':
        try:
            id = request.form['id']
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            correo = request.form['correo']
            password = request.form['password']
            telefono = request.form['celular']
            ciudad = request.form['ciudad']
            direccion = request.form['direccion']
            tipo = 2
         
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?)",(id,nombre,apellido,correo,hashlib.md5(password.encode()).hexdigest(),telefono,ciudad,direccion,tipo) )
                con.commit()
                con.close()
                msg = "Registro Exitoso"         
        except:
            con.rollback()
            msg = "Error"
        finally:
            return redirect(url_for('login.loginForm'))

