from django.urls import path
from v1.auth.views import *

from v1.views import MainView

urlpatterns =[
    path('register/', RegisView.as_view()),
    path('login/', LoginView.as_view()),
    path('', MainView.as_view() ),
    ]
