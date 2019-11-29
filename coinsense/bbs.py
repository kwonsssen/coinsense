#django import
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger , EmptyPage
from django.db.models import Q
import json
from bbs import models
from bk_bbs import models as bk_models

#App import
from account.forms import LoginForm, NotifyForm
from account.views import login_func
from account.models import NoticeList
from django_summernote.models import Attachment

#합치기 위해
from itertools import chain
from operator import attrgetter

from bk_bbs.module import CustomAnonymousUser


#모든 게시글 합침
def get_board():
    board = models.FreeBoard.objects.all()          #자유게시판
    na = models.NormalAnalysis.objects.all()        #시황분석
    ht = models.HoneyTip.objects.all()              #꿀팁
    fb = models.ForumBitCoin.objects.all()          #포럼 비트코인
    gb = models.Gallery.objects.all()               #갤러리
    uc = models.UserColumn.objects.all()            #유저칼럼
    
    mk = bk_models.MarketBoard.objects.all()        #판매게시판
    ev = bk_models.Event.objects.all()              #이벤트게시판
    ca = bk_models.CoinAnalysis.objects.all()       #bk코인분석
    ab = bk_models.Analysis.objects.all()           #bk시황분석
    vb = bk_models.Video.objects.all()              #동영상게시판
    nb = bk_models.News.objects.all()               #뉴스게시판
    ic = bk_models.ICORating.objects.all()          #ico게시판

    #chain함수로 모든 쿼리셋을 하나로 합치면서 views 내림차순으로 정렬하여 리턴
    all_board = sorted(chain(board, na,ht,fb,gb,uc,mk,ev,ca,ab,vb,nb,ic), key=attrgetter('views'), reverse=True)
    return all_board

#조회수 5위 게시글
def get_ranking():
    board = get_board()
    ranking = board[:5]
    return ranking

def get_notice():
    notice_list = models.Notice.objects.all().order_by('-id')[:5]    #공지사항
    return notice_list

class BoardListView(UserPassesTestMixin,View):
    model = None
    login_form = None
    success_url= None
    template_name = None
    create_url = ''
    read_url=''
    context={}
    title = None
    permission = None
    access_permission=None          #접근권한전용
    approval_url= None              #학회전용 승인 url
    check_model = None              #학회 승인 비지블 on/off

    #학회 리스트 접근여부 접근권한자에 따라 승인목록 on/off 택
    def get_check_model(self):
        if self.check_model is not None: #체크모델이 들어왔다면
            user = self.check_model.objects.filter(user=self.request.user).first() #유저가 학회에 신청했는지 확인한다.
            if user is not None:                                              #결과 None이 아니라면 객체가 있으므로 보여주면안됨
                self.context['check_r'] = False                               #결과 None이 맞다면 객체가 없으므로 보여줘야함
            else:
                self.context['check_r'] = True
        return None

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_permission(self):
        #아무 권한 부여 안하면 모두에게 개방
        if self.permission is None:
            return True
        #BK이면 모두 접근할수 있음
        if self.request.user.code =="BK":
            return True
        #그외 권한설정
        if self.request.user.code == self.permission:
            return True
        return False

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    def context_init(self):
        self.context['post_list'] = self.model.objects.all().order_by('id')
        self.context['form'] = self.login_form()
        self.context['boardtitle'] = self.title
        self.context['url']= reverse(self.create_url)
        self.context['read_url'] = self.read_url
        self.context['permission'] = self.get_permission()
        self.context['ranking_list']= get_ranking()
        if not self.request.user.username == 'AnonymousUser':
            self.context['event_list'] = NoticeList.objects.filter(user=self.request.user)
            self.context['event_count'] = NoticeList.objects.filter(user=self.request.user, is_read=False).count()
        #학회 승인 리스트 주소
        if self.approval_url is not None:
            self.context['approval_list']= reverse(self.approval_url)

    def get_serach(self):
        search = self.request.GET.get('search',None) #검색 가져오기
        #검색소스
        if search is not None: #검색이 있다면 
            self.context['post_list'] = self.context['post_list'].filter(
                title__contains=search) #필터해서 적용
    
    def get_pagination(self):
         #페이지 네이션

        paginator = Paginator(self.context['post_list'], 1) #숫자만큼씩 묶어 페이지 생성 선언
        
        page = self.request.GET.get('page',1 )
        
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
        #paginator=max(paginator.paginator.page_range)/1
        print(paginator.paginator.page_range)
        print(paginator.has_previous)
        print(max(paginator.paginator.page_range))
        
        
        self.context['post_list'] = paginator

        #10개단위 페이지 이동
        def next_page(page):
            if page+10>=max(paginator.paginator.page_range):
                return max(paginator.paginator.page_range)
            else:
                return page + 10
            return page + 10
        def before_page(page):
            if page-10<=1:
                return 1
            else:
                return page - 10

        # 1 page경우
        if int(page)==1:
            self.context['range'] = range(1,11)
        # last page경우
        elif int(page)==max(paginator.paginator.page_range):
            self.context['range'] = range(int(page)-9,int(page)+1)    
        # 현재 페이지+5가 마지막 페이지번호보다 큰경우
        elif int(page)+5 > max(paginator.paginator.page_range):
            self.context['range'] = range(max(paginator.paginator.page_range)-9,max(paginator.paginator.page_range)+1)    
        # 현재 페이지-5가 마지막 페이지번호보다 작은경우
        elif int(page)-5 < 1:
            self.context['range'] = range(1,11)    
        else:
            self.context['range'] = range(int(page)-5,int(page)+5)
        self.context['last_page'] = max(paginator.paginator.page_range)
        self.context['next_page'] = next_page(int(page))
        self.context['before_page'] = before_page(int(page))
        
        


    #get 요청일때
    def get(self, *args, **kwargs):
        self.context_init()
        self.get_serach()
        self.get_pagination()

        #승인신청 보여주기
        if self.request.user.is_authenticated: #로그인 대상에게 
            self.get_check_model()
        else:                                   #비로그인 대상
            pass

        self.context['notice_list'] = get_notice()
        self.context['notice'] = get_notice()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['permission'] = self.get_permission()
        self.context['notice_list'] = get_notice()
        return render(self.request, self.get_template_name(), self.context)


class BoardCreateView(UserPassesTestMixin, View):
    model = None
    form_class = None
    template_name = None
    context={}
    title = None
    access_permission = None
    notice_model = models.Notice
    bk = None     

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        self.context['form'] = self.form_class()
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking_list']= get_ranking()
        if not self.request.user.username == 'AnonymousUser':
            self.context['event_list'] = NoticeList.objects.filter(user=self.request.user)
            self.context['event_count'] = NoticeList.objects.filter(user=self.request.user, is_read=False).count()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None, self.request.FILES or None)
        if self.bk is not None: #bk 글쓰기라면
            if form.is_valid():
                bk_post = form.save(commit=False)
                bk_post.ico_id = self.kwargs['pk']
                bk_post.author = self.request.user
                bk_post.save()
                return redirect(bk_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post)
        return render(self.request, self.get_template_name(), self.context)

#게시글 디테일 뷰
class BoardReadView(View):
    model = None                    #게시글 모델
    comment_model = None            # 댓글 모델
    form_class = None               #로그인 폼
    comment_Form_class = None       #댓글 폼
    template_name = None            #템플릿 
    context={}  
    title = None                    #게시판이름
    like_url=''                     #좋아요 url
    dislike_url=''                  #싫어요 url
    update_url=''                   #수정 url
    destroy_url=''                  #삭제 url
    comment_url=''                  #댓글 url
    bookmark_url=None                 #북마크 url
    notice_model = models.Notice
    ico_bk_post=None                #ico_bk_post
    
    def get_ico_bk_post(self):
        post = get_object_or_404(self.model, id=self.kwargs['pk'] )     #본 게시판의 pk를 가져와서
        bk_post= self.ico_bk_post.objects.filter(ico=post).first()      #bk글이 있는지 확인한다. 없다면 None리턴
        if bk_post is not None:                                         #bk글이 있다면
            self.context['bk_post'] = bk_post                           #bk_post를 컨텐츠로 넣고
            return True                                                 #화면에 보여줄 조건으로 설정
        else:                                                           #없다면 
            return False                                                #화면에 보여주지 않는다.
        return False                                                   

    def get_comment_form(self):
        return self.comment_Form_class

    def get_comment_model(self):
        return self.comment_model.objects.all()
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        pk=self.kwargs['pk']
        forms = NotifyForm()
        post = get_object_or_404(self.model, id=pk )
        
        if not post.author == self.request.user:
            post.views = post.views+1
            post.save()
        
        self.context['notify_form'] = NotifyForm()
        self.context['post'] = post
        self.context['like_count'] = post.like_count
        self.context['dislike_count'] = post.dislike_count
        self.context['form'] = self.form_class 
        self.context['boardtitle'] = self.title
        self.context['comment_form'] = self.get_comment_form()
        self.context['comments'] = self.get_comment_model().filter(post=post)
        self.context['notice'] = self.notice_model.objects.all()
        if self.ico_bk_post is not None:
            self.context['bk_condition'] = self.get_ico_bk_post()
        #접근주소 가변처리
        self.context['like_url'] =  reverse(self.like_url)
        self.context['dislike_url'] = reverse(self.dislike_url)
        self.context['update_url'] = self.update_url
        self.context['destroy_url'] = self.destroy_url
        if self.comment_url != '':
            self.context['comment_url'] = reverse(self.comment_url)
        self.context['ranking_list']= get_ranking()
        if self.bookmark_url is not None:
            self.context['bookmark_url'] = reverse(self.bookmark_url)

        #알림 카운트
        if not self.request.user.username == 'AnonymousUser':
            self.context['event_list'] = NoticeList.objects.filter(user=self.request.user)
            self.context['event_count'] = NoticeList.objects.filter(user=self.request.user, is_read=False).count()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        pk=self.kwargs['pk']
        forms = NotifyForm(self.request.POST)
        post = get_object_or_404(self.model, id=pk )
        if forms.is_valid():
            notify = forms.save(commit=False)
            notify.user = self.request.user
            notify.post = post.title
            notify.board = self.title
            notify.save()
        
        self.context['error'] = login_func(self.request)   #로그인처리

        self.context['post'] = get_object_or_404(self.model, id= self.kwargs['pk'])
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        self.context['notify_form'] = forms #신고하기폼
        return render(self.request, self.get_template_name(), self.context)

#게시글 수정 뷰
class BoardUpdateView(UserPassesTestMixin, View):
    model = None
    form_class = None
    success_url= None
    template_name = None
    title = None
    context={}
    notice_model = models.Notice
    bk = None

    #작성자아니면 못들어온다.
    def test_func(self):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if self.request.user == post.author:
            return True
        return False

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.model, id=pk)

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name

    #form 인스턴스 생성
    def get_form(self):
        form_kwargs={
            'instance':self.get_object(),
        }
        if self.request.method == 'POST':
            form_kwargs.update({
                'data':self.request.POST,
                'files': self.request.FILES,
            })
        return self.form_class(**form_kwargs)

    #context에 넘길 변수 설정
    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form']= self.get_form()
        return kwargs

    #get 요청일때
    def get(self, *args, **kwargs):
        form_kwargs={
            'instance':self.get_object(),
        }
        self.context['boardtitle']=self.title
        self.context['form'] = self.form_class(**form_kwargs)
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking_list']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)
    
    #post 요청일때
    def post(self, *args, **kwargs):
        form = self.get_form()
        if self.bk is not None: #bk 글쓰기라면
            if form.is_valid():
                bk_post=form.save()
                return redirect(bk_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return redirect(post)
        return render(self.request, self.get_template_name(), self.get_context_data(form=form))

#ajax로 pk를받아드린다.
class BoardDestroyView(UserPassesTestMixin, View):
    model = None
    redirect_url = None
    #작성자아니면 못들어온다.
    def test_func(self):
        post = get_object_or_404(self.model, id=self.request.POST['pk'])
        if self.request.user == post.author:
            return True
        return True
    
    def post(self, *args, **kwargs):
        
        img_list=[]
        query_list=[]

        #attachement는 djangosummernote...로 시작 따라서 src로 받아온 문자열을
        #필터작업을 위해서 /media/ 제거
        for data in json.loads(self.request.POST.get('imgSrc')):
            img_list.append(data[7:])
        
        #필터링된 attachement 튜플 삭제
        #삭제시 파일삭제는 bbs.signals.py에서 정의된 함수로 신호를 보내 처리한다.
        for img in img_list:
            Attachment.objects.filter(file=img).delete()

        #post를 가져와서
        post = get_object_or_404(self.model, id=self.request.POST['pk'])

        #게시글도 삭제한다.
        post.delete()

        #게시판으로 돌아가도록 해당 주소를 리턴
        self.redirect_url = reverse(self.redirect_url)
        
        return HttpResponse(json.dumps(self.redirect_url))

#좋아요 ajax
class LikeView(View):
    model = None
    context={}

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk', None))

        #check_dislike 릴레이션에 해당 post 필터링 
        #필터링 결과중 첫 row를 가져온다. 못가져오면 None
        check_dislike = post.dislike_set.filter(post=post).first()
        
        # none이아니라면 즉 비추천을 적용했다면
        if check_dislike is not None:
            #아무것도하지말고 리턴
            return HttpResponse(json.dumps('no'))
        #none라면 추천 처리
        post_like, post_like_created = post.like_set.get_or_create(user=self.request.user)
        if not post_like_created:
            post_like.delete()
            message = "like_del"
        else:
            message = "like"
        context = {'like_count': post.like_count,
               'message': message,
               'username': self.request.user.nickname }
        return HttpResponse(json.dumps(context))

#싫어요 ajax
class DisLikeView(View):
    model = None
    context={}

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk', None))
        
        #check_like 릴레이션에 해당 post 필터링 
        #필터링 결과중 첫 row를 가져온다. 못가져오면 None
        check_like = post.like_set.filter(post=post).first()
        
        # none이아니라면 즉 추천을 적용했다면
        if check_like is not None:
            #아무것도하지말고 리턴
            return HttpResponse(json.dumps('no'))
        
        post_dislike, post_dislike_created = post.dislike_set.get_or_create(user=self.request.user)
        if not post_dislike_created:
            post_dislike.delete()
            message = "dislike_del"
        else:
            message = "dislike"

        context = {'dislike_count': post.dislike_count,
               'message': message,
               'username': self.request.user.nickname }
        return HttpResponse(json.dumps(context))

#북마크 AjaxView
class BookMarkView(View):
    model = None
    context={}

    #로그인한 사용자만 들어올 수 있다.
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #post 요청일때
    def post(self, *args, **kwargs):
        #프론트에서 받아온 pk를 통해 post를 가져온다.
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk', None))
        
        #해당 post의 bookmark_set으로 중간자 모델 bookmark에 접근하여 요청한 유저의 튜플을
        #가져오고, 없다면 만드는 작업을 수행한다. 
        post_bookmark, post_bookmark_created = post.bookmark_set.get_or_create(user=self.request.user)
        if not post_bookmark_created:
            post_bookmark.delete()
            message = "찜 등록"
        else:
            message = "찜 해제"

        context = {
               'message': message,
               }
        return HttpResponse(json.dumps(context))
#댓글생성
class CommentView(View):
    model = None
    form_class = None
    template_name=None
    context = {}
    

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #post 요청일때
    def post(self, *args, **kwargs):
        post = get_object_or_404(self.model, pk=self.request.POST.get('pk',None))
        form = self.form_class(self.request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = self.request.user
            com.post = post
            com.save()
            self.context['comment'] = com
            NoticeList.objects.create(user=post.author , content="{0} 게시글에 새로운 댓글이 달렸습니다.".format(post), link=post.get_absolute_url())
            return render(self.request, self.template_name, self.context)
        self.context['form']= form
        return render(self.request, self.template_name, self.context)

   

class ForumListView(View):
    model = None
    form_class = None
    success_url= None
    template_name = None
    context = {}
    title = None
    notice_model = models.Notice

    def get_success_url(self):
        return self.success_url
    
    def get_template_name(self):
        return self.template_name
    
    #get 요청일때
    def get(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['form'] = self.form_class()
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        self.context['ranking']= get_ranking()
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        #self.context['post_list'] = self.model.objects.all()
        self.context['error'] = login_func(self.request)
        self.context['boardtitle'] = self.title
        self.context['notice'] = self.notice_model.objects.all()
        
        return render(self.request, self.get_template_name(), self.context)

#승인목록/게시글 조회 ajax View
class SocietyApprovalView(UserPassesTestMixin,View):
    model = None                    #승인 릴레이션
    template_name=None              #템플릿
    context = {}                    #프론트로 넘겨줄 데이터
    access_permission=None          #접근권한
    accept_url = None               #수락 url
    reject_url = None               #거절 url
    read_url = None                 #게시글 조회때 사용하는 읽기 url

    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        if self.read_url is not None:
            self.context['read_url'] = self.read_url

        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url

        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        if self.read_url is not None:
            self.context['read_url'] = self.read_url

        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)


#승인 ajax
class SocietyAcceptView(UserPassesTestMixin,View):
    model = None
    template_name=None
    context = {}
    access_permission=None
    accept_url = None
    reject_url = None
    code = 'Z0'
    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all()
        pk = self.request.POST.get('pk',None)
        if pk is not None:
            user= user_list.filter(user=pk).first()
            if user is not None:
                user.user.code= self.code
                user.user.save()
                user.delete()
                

        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

#승인 거절 ajax
class SocietyRejectView(UserPassesTestMixin,View):
    model = None
    template_name=None
    context = {}
    access_permission=None
    accept_url = None
    reject_url = None
    code = 'Z0'
    
    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        user_list = self.model.objects.all()
        pk = self.request.POST.get('pk',None)
        if pk is not None:
            user= user_list.filter(user=pk).first()
            if user is not None:
                user.delete()

        user_list = self.model.objects.all().order_by('id')
        self.context['user_list'] = user_list
        self.get_pagination()
        self.context['accept_url'] = self.accept_url
        self.context['reject_url'] = self.reject_url
        return render(self.request, self.template_name, self.context)


from django.contrib.auth import get_user_model
#승인 거절 ajax
class SocietyRequestView(UserPassesTestMixin,View):
    model = None
    template_name=None
    context = {}
    form = None
    redirect_url= ''
    access_permission=None
    code = 'Z0'
    
    #접근조건 view사용시 pass조건을 정하지않으면 로그인한 누구나 접근이가능하고,
    #조건 선택시 해당 조건의 유저만 들어갈수있다.
    def test_func(self):
        if self.access_permission is None:
            return True
        if self.request.user.code == "BK":
            return True
        if self.request.user.code == self.access_permission:
            return True
        return False

    def get_pagination(self):
         #페이지 네이션
        paginator = Paginator(self.context['user_list'], 2) #15개씩 묶어 페이지 생성 선언

        page = self.request.GET.get('page',1 )
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)
            
        self.context['user_list'] = paginator

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.context['form'] = self.form
        return render(self.request, self.template_name, self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        pk = int(self.request.POST.get('user'))
        user_chk = self.model.objects.filter(user=self.request.user).first()

        user = get_user_model().objects.filter(pk=pk).first()
        if user_chk is None:
            form = self.form(self.request.POST)
            if form.is_valid():
                req = form.save(commit=False)
                req.user = user
                req.save()
                return HttpResponse('완료되었습니다.')
        else:
            return HttpResponse("실패했습니다.")
        return render(self.request, self.template_name, self.context)



#ajax로 기존 base내용은 유지한태로 특정 부위만 내용 교체기 때문에
#Colum에서 필요한 녀석들로 채우면 된다.
#ico에 colum이 있다면 보여줄 colum 모델 
#ico에 colum이 없다면 글이 없다고 보여줄 조건
#ico에 colum이 없을때 글쓰기 권한이 있는 자라면 보여줄 조건
class IcoColumAjaxReadView(View):
    model = None
    template_name = None            #템플릿 
    context={}  
    like_url=''                     #좋아요 url
    dislike_url=''                  #싫어요 url
    update_url=''                   #수정 url
    create_url=''
    destroy_url=''                  #삭제 url
    ico_colum_post=None             #ico_colum_post
    
    def get_ico_colum_post(self):
        post = get_object_or_404(self.model, id=self.kwargs['pk'] )     #본 게시판의 pk를 가져와서
        self.context['ico']= post
        colum_post = self.ico_colum_post.objects.filter(ico=post).first()     #bk글이 있는지 확인한다. 없다면 None리턴
        if colum_post is not None:                                         #bk글이 있다면
            self.context['column_post'] = colum_post                           #bk_post를 컨텐츠로 넣고
            return True                                                 #화면에 보여줄 조건으로 설정
        else:                                                           #없다면 
            return False                                                #화면에 보여주지 않는다.
        return False                                                   

    def get_comment_form(self):
        return self.comment_Form_class

    def get_comment_model(self):
        return self.comment_model.objects.all()
    
    def get_template_name(self):
        return self.template_name

    #get 요청일때
    def get(self, *args, **kwargs):
        self.context['create_url'] = self.create_url
        self.context['update_url'] = self.update_url
        self.context['like_url'] = self.like_url
        self.context['dislike_url'] = self.dislike_url
        if self.ico_colum_post is not None:
            self.context['bk_condition'] = self.get_ico_colum_post()
        print
        return render(self.request, self.get_template_name(), self.context)

    #post 요청일때
    def post(self, *args, **kwargs):
        return render(self.request, self.get_template_name(), self.context)

#GET 방식 보여주기 POST 작성하기
#GET 방식으로 접근시 해당 게시글의 PK를 받아드린다.
class IcoFreeOpinionView(View):
    model=None
    form_class=None
    template_name = None                                #템플릿 이름
    ico_model = None                                    #ico모델 
    comment_url = ''

    def get(self, *args, **kwrags):
        context={}
        pk = self.kwargs['pk']
        comment = self.model.objects.filter(post_id=pk).first()
        if comment is not None:
            context['comment_list'] = self.model.objects.all()
            context['com'] = True
        else:
            context['com'] = False
        context['post'] = pk
        context['comment_form'] = self.form_class
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        context={}
        self.template_name = 'bk_bbs/free_opinion_ajax.html'
        form = self.form_class(self.request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = self.request.user
            com.post_id = self.kwargs['pk']
            com.save()
            context['comment'] = com
        return render(self.request, self.template_name, context)
