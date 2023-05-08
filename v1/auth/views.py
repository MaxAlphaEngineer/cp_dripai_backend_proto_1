from v1.models.auth import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token




class RegisView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data

        nott = ["name", "mobile", "password"]
        s = ''

        for i in nott:
            if i not in data:
                s += f"{i}"
        if s:
            return Response({
                "Error": f" There is no {s} in data "})

        if len(data['mobile']) != 12:
            return Response({"Error": "Mobile phone must contain minimum 12 digits"})

        if not data['mobile'].isdigit():
            return Response({"Error": "Mobile number must be in digits ! "})

        if len(data['password']) < 6:
            return Response({"Error": "Password is too simple "})

        user = User.objects.create_user(
            name=data.get('name', ''),
            password=data.get('password', ''),
            mobile=data['mobile'],
        )
        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
        })



class LoginView(GenericAPIView):
    def post(self,  requests, *args, **kwargs):
        data = requests.data

        if data is None:
            return Response({
                "Error": "There is no data"
            })

        nott = 'mobile' if 'mobile' not in data else 'password' if "password" not in data else None
        if nott:
            return Response({
                "Error": f"{nott} is missing!"
            })
        user = User.objects.filter(mobile=data['mobile']).first()

        if not user:
            return Response({
                "Error": "There is not User with this number"
            })
        if not user.check_password(data['password']):
            return Response({
                "Error": "Password ERROR"
            })

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            "Success": token.key,
            "user": user.format()
        })






