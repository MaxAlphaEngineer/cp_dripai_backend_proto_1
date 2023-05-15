from v1.format import dataformat
from v1.models import SensorData
from methodism.helper import custom_response


def sensor_all(requests, params):
    sdata = SensorData.objects.all()
    return custom_response(True, data={"Result": [dataformat(x) for x in sdata]})


def sensor_add(requests, params):

    if "sensor_id" not in params:
        return custom_response(False, custom_response({"Error":"No sensor ID"}))

    if 'tuproq_nam1' not in params:
        return custom_response(False, message={"Error": "Namlik_1 not in data"})

    if 'tuproq_nam2' not in params:
        return custom_response(False, message={"Error": "Namlik_2 not in data"})

    if 'havo_nam' not in params:
        return custom_response(False, message={"Error": "havo_nam not in data"})

    if "havo_temp" not in params:
        return custom_response(False, message={"Error": "havo_temp not in data"})

    # if params['sensors'] is not list:
    #     return custom_response(False, message={"Error": "Sensors are not in list format"})
    #
    # if not params['sensors']:
    #     return custom_response(False, message={"Error": "List is empty"})

    sensordata = SensorData.objects.create( sensor_id=params["sensor_id"],tuproq_nam1=params['tuproq_nam1'], tuproq_nam2=params['tuproq_nam2'],
                                           havo_nam=params["havo_nam"], havo_temp=params["havo_temp"])

    sensordata.save()

    return custom_response(True, data={"Success":"Data added "})