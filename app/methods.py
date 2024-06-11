#importamos el metodo user para mostrar los usuarios
from .schemas.user import User
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
            print("Exito")
        else:
            print("Suerte la proxima")

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


def newUser(nombre, apellido, correo, contrasenia):
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("""
INSERT INTO users (nombre, apellido, correo, contraseña) VALUES(%s, %s, %s, %s)
    """, (nombre, apellido, correo, contrasenia))

    conn.commit()

    cursor.close()
    conn.close()

    
#Funcion para conectar con la DataBase por medio de la libreria psycopg2
def connection_db():
    global connection
    
    try:
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