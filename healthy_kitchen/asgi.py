"""
ASGI config for healthy_kitchen project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from main.consumers import ProductViewConsumer
from channels.routing import URLRouter,ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthy_kitchen.settings')

application = get_asgi_application()

wspatterns = [
        path('ws/productview/<id>/',ProductViewConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(wspatterns))
})
