from django.urls import path
from v1.views import MainView

urlpatterns =[

    path('method/', MainView.as_view() ),
    ]
