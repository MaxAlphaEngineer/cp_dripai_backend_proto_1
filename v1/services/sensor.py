from v1.format import dataformat
from v1.models import SensorData
from methodism.helper import custom_response


def sensor_all(requests, params):
    sdata = SensorData.objects.all()
    return custom_response(True, data={"Result": [dataformat(x) for x in sdata]})


def sensor_add(requests, params):
    if 'sensors' not in params:
        return custom_response(False, message={"Error": "Data isn't enough"})

    if params['sensors'] is not list:
        return custom_response(False, message={"Error": "Sensors are not in list format"})

    if not params['sensors']:
        return custom_response(False, message={"Error": "List is empty"})

def sensor_two(requests, params):
    a={
        "asfadkmg"
    }
    return custom_response(True, data=a)






