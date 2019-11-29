from .models import NoticeList
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from .models import Profil, Note

@receiver(post_save, sender=NoticeList)
def new_notice(sender, instance, created, **kwargs):
   
    if created:
        user_name = instance.user.username
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            user_name ,{
                "type":"user.event",
                "event": "New Event",
                "message" : instance.content,
                "link" : instance.link
                },
        )



            