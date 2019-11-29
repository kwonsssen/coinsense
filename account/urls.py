from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
    path('', views.index, name='index'),                                            #메인
    path('signup/', views.signup, name="signup"),                                   #회원가입                                   #
    path('logout/', auth_views.logout, name='logout',kwargs={'next_page':'/'}),     #로그아웃
    path('info/destroy/', views.myDestroy, name="destroy"),                         #회원탈퇴 페이지
    path('info/pw/', views.myPasswordUpdate, name="my_pw_update"),                   #비밀번호 수정 페이지
    path('note/' , views.note, name="note"),                                        #쪽지 보내기
    path('info/',views.myPage, name="my_page"),                                     #회원정보    
    path('info/ajax', views.myPageAjax, name="my_page_ajax"),                       #회원정보 ajax
    path('info/update', views.myUpdate, name="my_update"),                          #수정페이지
    path('info/write/',views.myWrite, name="my_write"),                             #내가쓴글
    path('info/comments/', views.myComments, name="my_com"),                        #내가쓴댓글
    path('info/posts/', views.MyPostSave, name="my_pos"),                           #내가쓴글
    path('info/messages/', views.myMessage, name="my_msg"),                        #내 쪽지함
    path('info/notice/', views.myNotice, name="my_notice"),                         #내 알림
    path('note/destroy/<int:pk>', views.noteDestroy, name="note_destroy"),                    #쪽지제거
    path('note/<int:pk>', views.noteRead, name="note_read"),                         #쪽지읽기
]