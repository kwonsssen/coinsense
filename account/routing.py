from django.conf.urls import url
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/notice/<slug:user_name>/',consumers.NoticeConsumer)
]