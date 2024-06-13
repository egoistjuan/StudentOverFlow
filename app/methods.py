#importamos el metodo user para mostrar los usuarios
from .schemas.user import User
from .schemas.questions import Question
#Libreria que nos de la conexion con la db
import psycopg2

def prueba_signIn(contrasenia):
    #lista = []
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("SELECT correo, contraseña FROM users WHERE contraseña = %s", (contrasenia,))
    Sign = cursor.fetchall()
    for i in Sign:
        if contrasenia == i[1]:
            return True
        else:
            return False

    cursor.close()
    conn.close()

def obtener_id(correo_user):
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE correo = %s", (correo_user,))
    usuario = cursor.fetchall()

    print(usuario)

    cursor.close()
    conn.close()

def mostrar_usuarios():
    listUsers = []
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id_user, nombre, apellido, correo, contraseña FROM users")

    users = cursor.fetchall()

    for userX in users:
        nuevoUser = User(userX[0], userX[1], userX[2], userX[3], userX[4])
        listUsers.append(nuevoUser)

    cursor.close()
    conn.close()

    return listUsers

def ver_preguntas():
    lista_preguntas = []
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id_question, question, id_user FROM questions")

    questions_1 = cursor.fetchall()

    for read in questions_1:
        questions_read = Question(read[0], read[1], read[2])
        lista_preguntas.append(questions_read)

    cursor.close()
    conn.close()

    return lista_preguntas


#Esta funcion sirve para crear usuarios nuevos
def newUser(nombre, apellido, correo, contrasenia):
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("""
INSERT INTO users (nombre, apellido, correo, contraseña) VALUES(%s, %s, %s, %s)
    """, (nombre, apellido, correo, contrasenia))

    conn.commit()

    cursor.close()
    conn.close()

def newQuestion(id, pregunta, id_usuario):
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute(""""
INSERT INTO questions (id_question, question, id_user) VALUES(%s, %s, %s)
                   """, (id, pregunta, id_usuario))
    
    conn.commit()

    cursor.close()
    conn.close()

    
#Funcion para conectar con la DataBase por medio de la libreria psycopg2
def connection_db():
    global connection
    
    try:
        #Aqui se hace la conexion para la DB de pgAdmin
        print('Loading connection')

        connection = psycopg2.connect(
            host = '172.25.48.1',
            database ='studentoverflow',
            user = 'clientes',
            password = 'password'
        )
        print('Connection succesful :)')
    
    except psycopg2.Error as error:
        print(error)

    return connection