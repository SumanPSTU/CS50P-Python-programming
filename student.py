class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if name not in ["sumon","arif","mridu"]:
            raise ValueError("Invalid name!")
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email = email