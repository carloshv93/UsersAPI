# no pruebes la class file no tiene nada que testear 

class TestUser:
    def test_init__(self,name:str,username:str,email:str, password:str):
        self._name = name
        self._username = username
        self._email = email
        self._password = password

    def test_actualizar(self,user):
        pass

    def test_actualizar_sin_valoresYdatos_erroneos(self):
        pass