import requests
from methodism.helper import custom_response

from cp_dripai_backend_proto_1.settings import WeatherAPIToken
from v1.models.weather import Weather


def weather_current(req, params):
    url = 'https://api.weatherapi.com/v1/current.json'
    token = WeatherAPIToken
    response = requests.post(url + "?key=" + token + "&q=" + params['q'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_forecast(req, params):
    url = 'https://api.weatherapi.com/v1/forecast.json'
    token = WeatherAPIToken
    response = requests.post(
        url + "?key=" + token + "&q=" + params['q'] + "&days=" + params['days'] + "&dt=" + params['dt'] + "&hour=" +
        params['h'] + "&lang=" + params['lang'] + "&alerts=" + params['al'] + "&aqi=" + params['aq'] + "&tp=" + params[
            'tp'])
    if response.status_code == 200:
        res = response.json()
        forecast = Weather.objects.create(user=req.user, location=res.get('location', {}), current=res.get('current', {}),
                            forecast=res.get('forecast', {}))

        return custom_response(True, data=forecast.response())
    else:
        return custom_response(False, message=response.text)


def weather_future(raq, params):
    url = 'https://api.weatherapi.com/v1/future.json'
    token = WeatherAPIToken
    response = requests.post(
        url + "?key=" + token + "&q=" + params['q'] + "&dt=" + params['days'] + "&lang=" + params['lang'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_history(raq, params):
    url = 'https://api.weatherapi.com/v1/history.json'
    token = WeatherAPIToken
    response = requests.post(
        url + "?key=" + token + "&q=" + params['q'] + "&dt=" + params['dt'] + "&unixdt" + params['unixdt'] + "&end_dt" +
        params['enddt'] + "&hour=" + params['h'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_marine(req, params):
    url = 'https://api.weatherapi.com/v1/marine.json'
    token = WeatherAPIToken
    response = requests.post(
        url + "?key=" + token + "&q=" + params['q'] + "&days=" + params['days'] + "&dt=" + params['dt'] + "&unixdt" +
        params['unixdt'] + "&hour=" + params['h'] + "&lang=" + params['lang'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_search(req, params):
    url = 'https://api.weatherapi.com/v1/search.json'
    token = WeatherAPIToken
    response = requests.post(url + "?key=" + token + "&q=" + params['q'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_timzone(req, params):
    url = 'https://api.weatherapi.com/v1/timezone.json'
    token = WeatherAPIToken
    response = requests.post(url + "?key=" + token + "&q=" + params['q'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)


def weather_astronomy(req, params):
    url = 'https://api.weatherapi.com/v1/astronomy.json'
    token = WeatherAPIToken
    response = requests.post(url + "?key=" + token + "&q=" + params['q'] + "&dt=" + params['dt'])
    if response.status_code == 200:
        return custom_response(True, data=response.json())
    else:
        return custom_response(False, message=response.text)
