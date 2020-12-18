class User:
    def __init__(self,name:str,username:str,email:str, password:str):
        self._name = name
        self._username = username
        self._email = email
        self._password = password

    def __repr__(self):
        return {"name":self._name,"username":self._username,"email":self._email,"password":self._password}
