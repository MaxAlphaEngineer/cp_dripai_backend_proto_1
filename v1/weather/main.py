import requests
api_key = "674948bd21f29583dfbb6d1884d97c08"

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/3.0/onecall?q={user_input}.04&exclude=hourly,daily&appid={api_key}")

print(weather_data.json())
if weather_data.json()['cod'] == 404:
    print("we can`t find your city")

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in: {user_input} is: {weather}")
    print(f"The temperature in: {user_input} is: {temp}F")

















