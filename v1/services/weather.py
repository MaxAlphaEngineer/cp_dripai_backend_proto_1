import requests
from methodism.helper import custom_response

from cp_dripai_backend_proto_1.settings import WeatherAPIToken


def weather_current(req, params):
    url = 'https://api.weatherapi.com/v1/current.json'
    token = WeatherAPIToken
    response = requests.post(url+"?key="+token+"&q="+params['q'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)



def weather_forecast(req, params):
    url = 'https://api.weatherapi.com/v1/current.json'
    token = WeatherAPIToken
    response = requests.post(url + "?key=" + token + "&q=" + params['q'] + "&days="+params['days'] + "&dt=" + "&hour=" + "&lang=" + "&tp=")
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


