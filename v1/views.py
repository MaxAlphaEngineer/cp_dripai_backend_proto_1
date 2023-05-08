from methodism.main import METHODIZM
from v1 import services


class MainView(METHODIZM):
    file = services
    not_auth_methods = ['sensor.all', 'sensor_add', 'login', 'regis']