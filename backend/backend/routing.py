from django.urls import path
from .consumers import RandomNumberConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

ws_urlpatterns = [
    path('ws/random_number/', RandomNumberConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        ws_urlpatterns
    ),
})