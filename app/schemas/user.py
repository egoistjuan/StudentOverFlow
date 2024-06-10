class User():
    def __init__(self, id_user, name, secondName, email, password):
        
        self.id_user = id_user
        self.name = name
        self.secondName = secondName
        self.email = email
        self.password = password
    
    def get_info(self):
        return {
            "id" : self.id_user,
            "name" : self.name,
            "secondName" : self.secondName,
            "email" : self.email,
            "password" : self.password
        }