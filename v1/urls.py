from v1.auth.views import *
from django.urls import path


urlpatterns =[
    path('register/', RegisView.as_view()),
    path('login/', LoginView.as_view()),

]