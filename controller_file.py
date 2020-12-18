from middleware_file import File
import json

class ControllerFile:
    def __init__(self,path:str):
        self._path = path

    def read(self):
        with File(self._path,"r") as _file:
            return _file.read()

    def save(self,data):
        self.write(data)
        with File(self._path,"w") as _file:
            _file.write(json.dumps(self._content))

    def write(self,data):
        self._content = data