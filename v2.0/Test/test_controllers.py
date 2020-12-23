from unittest import mock
from unittest.mock import MagicMock
from MVC.controllers import ControllerFile, ControllerUser
import pytest, tempfile
class TestControllerFile:

    # create
    @pytest.mark.parametrize("test_path,expected", [
        ("./Utils/existing_users.json", "./Utils/existing_users.json")
    ])
    def test_init(self,test_path,expected):
        controller = ControllerFile(test_path)

        path = expected

        assert isinstance(controller, ControllerFile)
        assert path == controller._path

    @pytest.mark.parametrize("test_path,expected", [
        ("", ""),
        ("existing_users.json", "existing_users.json")

    ])
    def test_invalid_init(self,test_path,expected):

        with pytest.raises(FileNotFoundError) as error:
            ControllerFile(test_path)
        assert expected in str(error.value)
 
    def test_read(self):
        file_mock = mock.mock_open()
        with mock.patch('__main__.open', mock.mock_open(read_data='input_values')) as file_mock:
            with open('path') as _:
                result = _.read()
        file_mock.assert_called_once_with('path')

        controller = ControllerFile('path') 
        result = controller.read()

        assert isinstance(result, str)
        assert result == 'input_values'
    # file = mock (class_style=File, return_vale="asd" )
    # test read write and save, en save debes validar en el metodo que pasa si viene vacio,
    # que no se pueda escribir en el file blanco / espacios vacios / un regex de caracteres especiales que solo Aa-Zz @ - _ . y 0-9 


class TestControllerUser:

    def test_read(self):
        pass
        #REAL
        #MOCK

        #EUEJUTA
        #RESULTADO
        #COMPARA