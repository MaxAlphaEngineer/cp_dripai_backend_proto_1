import os

import django
from channels.http import AsgiHandler

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,  URLRouter
from v1.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": AuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            ),
    }
)