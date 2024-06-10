#importamos el metodo user para mostrar los usuarios
from .schemas.user import User
#Libreria que nos de la conexion con la db
import psycopg2

def mostrar_usuarios():
    listUsers = []
    conn = connection_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id_user, nombre, apellido, correo, contraseña FROM users")

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        nuevoUser = User(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])
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