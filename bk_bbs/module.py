from django.contrib.auth.models import AnonymousUser as DjangoAnonymousUser

class CustomAnonymousUser(DjangoAnonymousUser):
    code = 'Z0'
    username= 'AnonymousUser'
    def __init__(self, request):
        super(CustomAnonymousUser, self).__init__()