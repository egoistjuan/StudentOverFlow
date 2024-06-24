# StudentOverFlow

--Proyecto basado en el sitio web llamado "Stack OverFlow"--

Para este proyecto se baso en la idea de crear una aplicacion web para estudiantes con preguntas y respuestas de los usuarios

---Es necesario instalar los requerimientos y creacion de la base de datos para su correcto funcionamiento---

-Para instalar las librerías, ejecutar el siguiente comando:

    pip install -r requirements.txt

# Base de Datos
--La db se debe conformar de 3 tablas, una para los usuarios y 2 relacionadas mediante una foreign-key

|      usuario       |      
|--------------------|      
|id_user   |SerialKey|      
|nombre    |         |      
|apellido  |         |      
|correo    |         |      
|contraseña|         |


|       questions      |
|----------------------|
|id_user    |ForeignKey|
|id_pregunta|SerialKey |
|question   |          |


|        answers        |
|-----------------------|
|id_respuesta|SerialKey |
|id_user     |ForeignKey|
|id_pregunta |ForeignKey|
|respuesta   |          |