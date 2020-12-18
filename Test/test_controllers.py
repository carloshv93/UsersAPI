from unittest import mock
from MVC.controllers import ControllerFile, ControllerUser

class TestControllerFile:
    # create
    def test_init(self):
        controller = ControllerFile('existing_users.json')

        path = 'existing_users.json' 

        assert isinstance(controller, ControllerFile)
        assert path == controller._path

    def test_init_novalues(self):
        pass 
    # que pasa cuando CF() vacio

    # test read write and save, en save debes validar en el metodo que pasa si viene vacio,
    # que no se pueda escribir en el file blanco / espacios vacios / un regex de caracteres especiales que solo Aa-Zz @ - _ . y 0-9 


class TestControllerUser:

    # todos los metodos, y si alguno tiene 2 caminos logicos su contraparte

    pass