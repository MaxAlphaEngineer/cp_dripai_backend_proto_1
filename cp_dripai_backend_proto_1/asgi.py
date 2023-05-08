
import os
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cp_dripai_backend_proto_1.settings')
django.setup()


application = get_default_application()
