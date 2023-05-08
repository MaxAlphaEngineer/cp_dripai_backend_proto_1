from methodism.helper import custom_response
from rest_framework.authtoken.models import Token

from v1.models import User


def regis(requests, params):
    data = params

    nott = ["name", "mobile", "password"]
    s = ''

    for i in nott:
        if i not in data:
            s += f"{i}"
    if s:
        return custom_response(False, message= f" There is no {s} in data ")

    if len(data['mobile']) != 12:
        return custom_response(False, "Mobile phone must contain minimum 12 digits")

    if not data['mobile'].isdigit():
        return custom_response(False, message= "Mobile number must be in digits ! ")

    if len(data['password']) < 6:
        return custom_response( False, message="Password is too simple ")

    user = User.objects.create_user(
        name=data.get('name', ''),
        password=data.get('password', ''),
        mobile=data['mobile'],
    )
    token = Token.objects.get_or_create(user=user)[0]

    return {
        "Success": token.key,
    }

def login(requests, data):

    if data is None:
        return custom_response(False, message="There is no data")

    nott = 'mobile' if 'mobile' not in data else 'password' if "password" not in data else None
    if nott:
        return custom_response(False, message= f"{nott} is missing!")

    user = User.objects.filter(mobile=data['mobile']).first()

    if not user:
        return custom_response(False,message= "There is no User with this number")


    if not user.check_password(data['password']):
        return custom_response(False, message="Password ERROR")



    token = Token.objects.get_or_create(user=user)[0]

    return custom_response(True, data={
        "Success": token.key,
        "user": user.format()
    })









