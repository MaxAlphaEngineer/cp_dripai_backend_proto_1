from django.urls import path
from v1.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    # url(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
    path('api/sensor', TicTacToeConsumer.as_asgi()),
]