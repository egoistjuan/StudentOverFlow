from flask import Blueprint, render_template, redirect, url_for, request, flash
from .methods import *

main = Blueprint('main', __name__)

@main.route('/')
def principal_page():

    return render_template('index.html')

@main.route('/prueba')
def prueba_user():
    
    preguntas_obtenidas = ver_preguntas()

    return render_template('questions.html', questions_1=preguntas_obtenidas)

@main.route('/register')
def registrarse():
     
     return render_template('register.html')

@main.route('/signIn_now', methods=['POST'])
def buscar():
    
    correo_usuario = request.form.get('uName')
    password = request.form.get('password_login')
    sucess = prueba_signIn(password)

    if sucess:
        obtener_id(correo_usuario)
        return redirect(url_for('main.usuario'))
        
    else:
        flash('Contraseña incorrecta')
        return redirect(url_for('main.signIn'))

@main.route('/usuario')
def usuario():

    return render_template('user.html')

@main.route('/signin')
def signIn():
    

    return render_template('signin.html')

#Ruta para crear al usuario
@main.route('/new_user', methods=['POST'])
def agregarUser():

    username = request.form.get('uName')
    secondname = request.form.get('secondName')
    correo_user = request.form.get('uEmail')
    contrasenia = request.form.get('contrasenia')

    newUser(username, secondname, correo_user, contrasenia)

    return redirect(url_for('main.principal_page'))