class Answers():
    def __init__(self, id_answer, respuesta, id_question, id_user):
        self.id = id_answer
        self.respuesta = respuesta
        self.id_question = id_question
        self.id_user = id_user

    def get_answers(self):
        return{
            "id_answer" : self.id,
            "respuesta" : self.respuesta,
            "id_question" : self.id_question,
            "id_user" : self.id_user

        }