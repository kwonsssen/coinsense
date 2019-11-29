#django
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, get_user_model, authenticate, update_session_auth_hash
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage
from django.core import serializers     #직렬화
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
#app
from bbs import models
from bk_bbs import models as bk_models
from .forms import LoginForm, UserCreationForm, UserUpdateForm, NoteForm
from bbs.models import FreeBoard
from .models import Note, NoticeList

#Python 
from itertools import chain
from operator import attrgetter


#코인가격 API받아오기위한
import json
import urllib.request
from urllib.request import Request, urlopen
import time



def coinnest_price():
    #코인네스트
    request = Request('https://api.coinnest.co.kr/api/pub/tickerall' , headers={'User-Agent': 'Mozilla/5.0'})
    read = urlopen(request).read()
    jsons = json.loads(read)
    coinnest_btc = int(jsons['KRW_BTC']['last'])
    coinnest_eth = int(jsons['KRW_ETH']['last'])
    coinnest_ltc = int(jsons['KRW_LTC']['last'])
    coinnest_etc = int(jsons['KRW_ETC']['last'])
    coinnest_bch = int(jsons['KRW_BCH']['last'])
    coinnest_qtum = int(jsons['KRW_QTUM']['last'])
    coinnest_price = [coinnest_btc, coinnest_eth, coinnest_ltc, coinnest_etc,'-', coinnest_bch,'-', coinnest_qtum,'-','-']
    return coinnest_price

def cashierest_price():
    #캐셔레스트
    request = Request('https://rest.cashierest.com/public/ticker/all' , headers={'User-Agent': 'Mozilla/5.0'})
    read = urlopen(request).read()
    jsons = json.loads(read)
    #print(jsons)
    cashierest_btc = int(float(jsons['ReturnData']['KRW_BTC']['last']))
    cashierest_eth = int(float(jsons['ReturnData']['KRW_ETH']['last']))
    cashierest_bch = int(float(jsons['ReturnData']['KRW_BCH']['last']))
    cashierest_eos = int(float(jsons['ReturnData']['KRW_EOS']['last']))
    cashierest_trx = int(float(jsons['ReturnData']['KRW_TRX']['last']))
    cashierest_price = [cashierest_btc, cashierest_eth, '-', '-','-', cashierest_bch,'-', '-',cashierest_eos,cashierest_trx]
    return cashierest_price

def get_pagination(model_list, bundle, page):
        #페이지 네이션
    paginator = Paginator(model_list, bundle) #15개씩 묶어 페이지 생성 선언

    try:
        paginator = paginator.page(page)
    except PageNotAnInteger:
        paginator = paginator.page(1)
    except EmptyPage:
        paginator = paginator.page(paginator.num_pages)

    return paginator

def get_my_post(pk):
    board = models.FreeBoard.objects.filter(author=pk)          #자유게시판
    na = models.NormalAnalysis.objects.filter(author=pk)        #시황분석
    ht = models.HoneyTip.objects.filter(author=pk)              #꿀팁
    fb = models.ForumBitCoin.objects.filter(author=pk)          #포럼 비트코인
    gb = models.Gallery.objects.filter(author=pk)               #갤러리
    uc = models.UserColumn.objects.filter(author=pk)            #유저칼럼
    
    mk = bk_models.MarketBoard.objects.filter(author=pk)        #판매게시판
    ev = bk_models.Event.objects.filter(author=pk)              #이벤트게시판
    ca = bk_models.CoinAnalysis.objects.filter(author=pk)       #bk코인분석
    ab = bk_models.Analysis.objects.filter(author=pk)           #bk시황분석
    vb = bk_models.Video.objects.filter(author=pk)              #동영상게시판
    nb = bk_models.News.objects.filter(author=pk)               #뉴스게시판
    ic = bk_models.ICORating.objects.filter(author=pk)          #ico게시판

    #chain함수로 모든 쿼리셋을 하나로 합치면서 views 내림차순으로 정렬하여 리턴
    all_board = sorted(chain(board, na,ht,fb,gb,uc,mk,ev,ca,ab,vb,nb,ic), key=attrgetter('created_at'), reverse=True)
    return all_board

def get_my_comment(pk):
    na = models.NormalAnalysisComment.objects.filter(author=pk)
    ht = models.HoneyTipComment.objects.filter(author=pk)
    fb = models.ForumBitCoinComment.objects.filter(author=pk)
    gb = models.GalleryComment.objects.filter(author=pk)
    uc= models.UserColumnComment.objects.filter(author=pk)
    su = models.SeoulUnvComment.objects.filter(author=pk)
    board =models.FreeBoardComment.objects.filter(author=pk)

    icbk = bk_models.ICORatingBkComment.objects.filter(author=pk)
    nb =bk_models.NewsComment.objects.filter(author=pk)
    mb = bk_models.MarketBoardComment.objects.filter(author=pk)
    eb = bk_models.EventComment.objects.filter(author=pk)
    ca = bk_models.CoinAnalysisComment.objects.filter(author=pk)
    ab = bk_models.AnalysisComment.objects.filter(author=pk)
    vb = bk_models.VideoComment.objects.filter(author=pk)
    ic = bk_models.ICORatingComment.objects.filter(author=pk)
    all_com = sorted(chain(board, na,ht,fb,gb,uc,su,mb,ca,ab,vb,nb,ic,icbk,eb), key=attrgetter('created_date'), reverse=True)
    return all_com


def login_func(request):
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
    else:
        username = False
        password = False
    user= authenticate(request, username=username,password=password)
    if user is not None:
        login(request, user)
        user = get_user_model().objects.get(pk=request.user.id)
        user.last_login=timezone.now
        
        #장기 로그인 여부 체크박스 확인 체크되었다면 임시로 일주일간 로그인유지
        if request.POST.get('login_for'):
            if request.POST['login_for']:
                request.session.set_expiry(604800)
        return ''
    else:
        return '아이디/비밀번호가 틀렸습니다.'
        

from coinsense import bbs
def index(request,context={}):
    '''
    coinnest = coinnest_price()
    cashierest = cashierest_price()
'''
    if request.method == "POST":        
        form = LoginForm(request.POST)
        context['error']= login_func(request)
    form = LoginForm()
    context['form'] = form
    context['post_list'] = FreeBoard.objects.all().order_by('-id')
    context['notice'] = models.Notice.objects.all()
    context['ranking_list']= bbs.get_ranking()
    '''
    context['coinnest_price']= coinnest
    context['cashierest_price']= cashierest
    '''

    #회원이 아닐 때 
    if not request.user.username == 'AnonymousUser':
        context['event_list'] = NoticeList.objects.filter(user=request.user)
        context['event_count'] = NoticeList.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'account/index.html', context)

def signup(request,context={}):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            login_func(request)
            print("로그인완료?")
            return redirect('account:index')
        else:
            print("로그인실패?")
            context['form'] = form

    if request.method =="GET":
        form = UserCreationForm()
        context['form']=form

    return render(request, 'account/signup.html', context)

@login_required
def myPage(request):
    context={}
    context['notice'] = models.Notice.objects.all()
    context['ranking_list']= bbs.get_ranking()
    note_count = Note.objects.filter(is_read=False).count()
    context['note_count'] = note_count
    
    context['event_list'] = NoticeList.objects.filter(user=request.user)
    context['event_count'] = NoticeList.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'account/my_page.html',context)

#내 정보 수정 페이지
@login_required
def myUpdate(request):
    context={}
    if request.method == "POST":
        data ={'in_short':request.user.in_short}        
        form = UserUpdateForm(request.POST, request.FILES, data, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/info/')
    data ={
        'in_short':request.user.in_short,
        'email':request.user.user_of.email,
        'phone_num':request.user.user_of.phone_number,
        'address': request.user.user_of.address,
        }
    context['form'] = UserUpdateForm(initial=data)
    return render(request, 'account/my_page_update.html', context)

#비밀번호 수정 페이지
@login_required
def myPasswordUpdate(request):
    context={}
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, "패스워드 변경에 성공했다.")
            return redirect('/info/')
        else:
            messages.error(request, '패스워드 변경 실패')
    else:
        form = PasswordChangeForm(request.user)
    context['form'] = form 
    return render(request, 'account/my_page_update.html',context)

#회원탈퇴
@login_required
def myDestroy(request):
    context={}
    if request.method == "POST":
        request.user.delete()
        return redirect('/')
    return render(request, 'account/account_destroy.html',context)
        
#내가쓴글
@login_required
def myWrite(request):
    post_list = get_my_post(request.user.pk)
    page = request.GET.get('page', 1)
    post_list = get_pagination(post_list, 5 , page)
    context={'post_list':post_list}
    return render(request, 'account/my_page_mypost.html',context)

#내가 작성한 댓글
@login_required
def myComments(request):
    comment_list = get_my_comment(request.user.pk)
    page = request.GET.get('page',1 )
    comment_list = get_pagination(comment_list, 5, page)
    context={'comment_list': comment_list}
    return render(request, 'account/my_page_mycomment.html',context)

#글저장함
@login_required
def MyPostSave(request):
    context={}
    bookmark_list = request.user.bookamrk_set.filter(user=request.user).all()
    context['bookmark_list'] = bookmark_list
    return render(request, 'account/my_page_postsave.html', context)

#마이페이지 ajax
@login_required
def myPageAjax(request):
    context={}

    return render(request, 'account/my_page_ajax.html',context)



#알림목록
@login_required
def myNotice(request,context={}):
    context['event_list'] = NoticeList.objects.filter(user=request.user)
    context['event_count'] = NoticeList.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'account/my_page_Notice.html', context)

#쪽지함
@login_required
def myMessage(request):
    context={}
    note_list = Note.objects.filter(receive_user=request.user)
    context['note_list'] = note_list
    return render(request, 'account/my_page_message.html', context)

#쪽지 생성
@login_required
def note(request):
    context={}
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.send_user = request.user
            note.save()
            NoticeList.objects.create(user=note.receive_user , content="{0}님께 쪽지 받음".format(request.user), link=note.get_absolute_url())
            return redirect('/')
    form = NoteForm()
    context['form']= form
    context['event_list'] = NoticeList.objects.filter(user=request.user)
    context['event_count'] = NoticeList.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'account/note_create.html', context)

@login_required
def noteDestroy(request, pk):
    if request.method == "POST":
        Note = get_object_or_404(Note, pk=pk)
        Note.delete()
    return redirect('/info/')

@login_required
def noteRead(request, pk):
    context={}
    note = get_object_or_404(Note, pk=pk)
    if not note.is_read:
        note.is_read = True
    note.save()
    context['note']=note
    context['event_list'] = NoticeList.objects.filter(user=request.user)
    context['event_count'] = NoticeList.objects.filter(user=request.user, is_read=False).count()
    return render(request, 'account/note_read.html',context)