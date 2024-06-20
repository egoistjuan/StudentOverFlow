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
    
    correo_usuario = request.form.get('uName_login')
    password = request.form.get('password_login')
    sucess = prueba_signIn(password)

    if sucess:
        print(correo_usuario)

        return redirect(url_for('main.usuario', correo=correo_usuario))
        
    else:
        flash('Contraseña incorrecta!')
        return redirect(url_for('main.signIn'))



@main.route('/usuario/<correo>')
def usuario(correo):

    info = obtener_id_por_email(correo)
    print(info)
    preguntas_usuarios = ver_preguntas()
    print(preguntas_usuarios)

    return render_template('user.html', data=info, questions_2=preguntas_usuarios)

@main.route('/usuario/<correo>/question/<id>')
def pregunta(correo, id):
    
    info_usuario = obtener_id_por_email(correo)
    print(info_usuario)
    pregunta_info = buscar_pregunta_id(id)
    print("-----------")
    respuesta_q = ver_respuestas(id)
    print(respuesta_q)
    print("---------")

    return render_template('answers.html',data_u=info_usuario, answers=respuesta_q, data_q=pregunta_info)

@main.route('/usuario/createQuestion/<correo>')
def createQuestion(correo):

    info_user = obtener_id_por_email(correo)

    return render_template('create_question.html', datos=info_user)

@main.route('/signin')
def signIn():
    

    return render_template('signin.html')



@main.route('/usuario/<correo>/question/<id>/createAnswer')
def createAnswer(correo, id):

    info_user = obtener_id_por_email(correo)
    info_question = buscar_pregunta_id(id)

    return render_template('create_answer.html', data_q=info_question, data=info_user)

#Ruta para crear al usuario
@main.route('/new_user', methods=['POST'])
def agregarUser():

    username = request.form.get('uName')
    secondname = request.form.get('secondName')
    correo_user = request.form.get('uEmail')
    contrasenia = request.form.get('contrasenia')

    newUser(username, secondname, correo_user, contrasenia)

    return redirect(url_for('main.principal_page'))

@main.route('/usuario/createQuestion/data', methods=['POST'])
def agregarPregunta():
    
    pregunta_1 = request.form.get('questionX')
    id_usuario = request.form.get('user_id')

    newQuestion(pregunta_1, id_usuario)

    return redirect(url_for('main.signIn'))

@main.route('/usuario/createAnswer/data', methods=['POST'])
def agregarRespuesta():
    
    id_user = request.form.get('id_user')
    question = request.form.get('id_q')
    respuesta = request.form.get('answer')

    newAnswer(respuesta, question, id_user)

    return redirect(url_for('main.signIn'))