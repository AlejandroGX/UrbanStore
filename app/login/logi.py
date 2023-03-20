import sqlite3, hashlib
from flask import render_template, request, url_for, redirect, abort, session
from . import login
from notifypy import Notify
from werkzeug.security import generate_password_hash, check_password_hash
 
login.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'
"""@login.route('/login', methods= ["GET", "POST"])
def log():
    notificacion = Notify()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM admin WHERE email='"+email+"' and password='"+password+"'")
        user = cur.fetchall()
        cur.execute("SELECT * FROM users WHERE correo_user='"+email+"' and id_user='"+password+"'")
        user2 = cur.fetchall()
        
        if len(user or user2) == 0:
            notificacion.title = "Error de Acceso"
            notificacion.message="Correo o contraseña no valida"
            notificacion.send()
            abort(401)
        else:
            if user:
                #cur.execute("SELECT nom_admin FROM admin WHERE email='"+email+"'")
                #nom_admin = cur.fetchone()
                return redirect(url_for('administrador.adm'))
            else:
                return redirect(url_for('usuarios.usu'))
    else:
        return render_template("login.html")
    """


@login.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('ini'))
    else:
        return render_template('login.html', error='')
    
@login.route("/login", methods = ['POST', 'GET'])
def logi():
    notificacion = Notify()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM admin WHERE email='"+email+"' and password='"+password+"'")
        admi = cur.fetchall()
        if admi:
            if len(admi) == 0:
                notificacion.title = "Error de Acceso"
                notificacion.message="Correo o contraseña no valida"
                notificacion.send()
                abort(401)
            else:
                return redirect(url_for('administrador.adm'))
              
        elif is_valid(email, password):
            session['email'] = email
            return redirect(url_for('ini'))
        else:
            notificacion.title = "Error de Acceso"
            notificacion.message="Correo o contraseña no valida"
            notificacion.send()
            abort(401)
        
def is_valid(email, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM users')
    data = cur.fetchall()
    """cur.execute("SELECT * FROM admin WHERE email='"+email+"' and password='"+password+"'")
    adm = cur.fetchall()
    if adm:
        if len(adm) == 0:
            return False
        else:
            return True
    else:"""    
    for row in data:
        if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
            return True
    return False

"""def is_valid2(email, password):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM admin')
    data2 = cur.fetchall()
    for row in data2:
        if row[0] == email and row[1] == password:
            return True
    return False"""

""""@login.route('/login', methods=['GET', 'POST'])
def log():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    if 'conectado' in session:
        return render_template('./index.html', dataLogin = dataLoginSesion())
        
    else:
        msg = ''
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            email      = str(request.form['email'])
            password   = str(request.form['password'])
            auth = request.authorization
                  
                
            # Comprobando si existe una cuenta
            cursor = cur.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admin WHERE email = ?", [email])
            account = cursor.fetchone()

            if account:
                if check_password_hash(account['password'],password):
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
                    session['conectado']       = True
                    session['id_admin']        = account['id_admin']
                    session['nom_admin']       = account['nom_admin']
                    session['ape_admin']       = account['ape_admin']
                    session['email']           = account['email']
                    session['tel_admin']       = account['tel_admin']
                    session['password']        = account['password']
                    session['tipo']            = account['tipo']

                    msg = "Ha iniciado sesión correctamente."
                    return redirect(url_for('administrador.adm'))
                    #render_template('./index.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion()) 

                else:
                    msg = 'Datos incorrectos, por favor verfique!'
                    return render_template("login.html")
                    #return render_template('login.html', msjAlert = msg, typeAlert=0)
            else:
                return abort(401),render_template('login.html', msjAlert = msg, typeAlert=0)
            
    return render_template('login.html', msjAlert = 'Debe iniciar sesión.', typeAlert=0)

def dataLoginSesion():
    inforLogin = {
        "id"                  :session['id_admin'],
        "nombre"              :session['nom_admin'],
        "apellido"            :session['ape_admin'],
        "emailLogin"          :session['email'],
        "telefono"            :session['tel_admin'],
        "password"            :session['password'],
        "tipoLogin"           :session['tipo']
    }
    return inforLogin
    """

