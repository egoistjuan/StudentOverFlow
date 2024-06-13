class Question():
    def __init__(self,id_pregunta, pregunta, id_usuario):
        self.id_pregunta = id_pregunta
        self.pregunta = pregunta
        self.id_usuario = id_usuario

    def get_question(self):
        return  {
            "id_pregunta" : self.id_pregunta,
            "pregunta" : self.pregunta,
            "id_usuario" : self.id_usuario

        }