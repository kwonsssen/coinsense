import os
import uuid

from django.db import models
from django.dispatch import receiver

from django_summernote.models import Attachment

@receiver(models.signals.post_delete, sender=Attachment)
def auto_delete_file_on_delete(sender, instance, **kwrags):
    
    #게시판당 하나씩 ptr로 attachment와 관계를 가지고 있었음... 그 튜플이 post삭제시 cascade 삭제가 되는데
    #관계형으로 맺은 튜플은 file이 없기 때문에 아래와 같이 instance.file.path를 하게되면 에러 폭팔
    #따라서 예외처리가 필요하게 되었고
    #파일업로드하지 않았다면. name이 Null 파이썬에선 None으로 표시되기때문에
    #아래와 같이 1차적인 예외처리를 진행
    if not instance.name is None:
        #디비에 저장된 path가 파일이 맞는지
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
