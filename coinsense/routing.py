# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import account.routing
from django.urls import path

#모든 요청(http/websocket 등)은 routing파일로오지만 
#프로토콜 타입 라우터에 http 요청에 대한 앱 셋팅을 하지 않으면
#기본적으로 장고 셋팅을 사용한다.
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            account.routing.websocket_urlpatterns
        )
    ),
})