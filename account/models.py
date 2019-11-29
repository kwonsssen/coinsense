# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.urls import reverse
#입력필드: id, password(상속), 닉네임, 사진, 한마디

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, nickname, password, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')

        username = self.model.normalize_username(username)
        user = self.model(username=username, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user.is_superuser:
            Profil.objects.create(user=user)
        return user

    def create_user(self, username, nickname=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, nickname, password, **extra_fields)

    def create_superuser(self, username, nickname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('code','BK')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, nickname, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    #입력필드: id, password(상속), 닉네임, 사진, 한마디
    #자동입력 필드: 레벨, 포인트, 경험치, 유저코드

    #id
    username = models.CharField(
        verbose_name=_('username'),
        max_length=30,
        unique=True,
    )

    #닉네임
    nickname = models.CharField(
        verbose_name=_('닉네임'),
        max_length=30,
        unique=True,
        blank=False,
    )
    
    #사진
    Photo = models.ImageField(
        verbose_name=_('프로필 사진'),
        upload_to="account/%Y/%m/%d",
        blank=True,
        null=True,
    )

    #한마디
    in_short= models.CharField(
        verbose_name=_('한마디'),
        max_length=255,
        blank=True,
    )

    #레벨
    level = models.IntegerField(
        verbose_name=_('level'),
        default=1
    )

    #유저코드
    code = models.CharField(
        verbose_name=_('code'),
        max_length=30,
        default='Z0',
    )
    #경험치
    exp = models.IntegerField(
        verbose_name=_('In short'),
        default=0,
    )
    #포인트
    point = models.IntegerField(
        verbose_name=_('Point'),
        default=0,
    )

    #가입날짜
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )
    
    last_login = models.DateTimeField(
        verbose_name=_('last login'),
        default=timezone.now
    )

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.nickname

    def get_full_name(self):        
        return self.nickname

    def get_short_name(self):
        return self.nickname
    def delete(self):
        self.Photo.delete()
        super(User,self).delete()

    get_full_name.short_description = _('Full name')

class Profil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_of',
    )

    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        blank=True
    )

    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        max_length=12,
    )

    address = models.TextField(
        verbose_name=_('Address'),
        blank=True
    )

    
#신고하기
class notify(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    board = models.CharField(verbose_name="board",max_length=20)
    post = models.CharField(verbose_name="title",max_length=40)
    content = models.CharField(verbose_name="신고 사유 ",max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Note(models.Model):
    send_user = models.ForeignKey(User ,on_delete=models.CASCADE,  related_name='send_user')
    receive_user = models.ForeignKey(User ,on_delete=models.CASCADE,  related_name='recive_user',)
    content = models.TextField("내용",blank=False,)
    send_del = models.BooleanField(default=False,)
    recive_del = models.BooleanField(default=False,)
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('account:note_read', args=[self.id])

class NoticeList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)        #알림받아야 하는 유저
    content = models.TextField()                                    #알림내용
    link = models.CharField(max_length=128)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)