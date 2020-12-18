from unittest import mock
from controller_file import ControllerFile

class TestControllerFile:
    # create
    def test_init(self):
        controller = ControllerFile('existing_users.json')

        path = 'existing_users.json'

        assert isinstance(controller, ControllerFile)
        assert path == controller._path
