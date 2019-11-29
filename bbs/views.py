from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
import json
from django.db.models import Q

#App 
from coinsense.bbs import BoardCreateView, BoardListView, BoardReadView, BoardUpdateView, BoardDestroyView, LikeView, DisLikeView, CommentView, ForumListView, SocietyApprovalView,SocietyAcceptView, SocietyRejectView, SocietyRequestView, BookMarkView
from . import models
from . import forms
from account.forms import LoginForm

# 게시판 필요 View 
# BoardCreateview, BoardListView, BoardReadView, BoardUpdateView, 
# BoardDestroyView, LikeView, DisLikeView, CommentView 총 8개

#자유게시판
freeList = BoardListView.as_view(
    model = models.FreeBoard,
    login_form = LoginForm ,
    success_url = '/free/',
    template_name='Board_List.html',
    create_url = 'bbs:free_create',
    read_url='bbs:free_read',
    title ="자유게시판",
)

freeCreate = BoardCreateView.as_view(
    model = models.FreeBoard,
    form_class = forms.FreeBoardCreationForm,
    template_name='Board_Create.html',
    title ="자유게시판 게시글 작성"
)

freeRead = BoardReadView.as_view(
    model = models.FreeBoard,
    comment_model = models.FreeBoardComment,
    comment_Form_class =  forms.FreeBoardCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="자유게시판",
    like_url='bbs:free_like',
    dislike_url='bbs:free_dislike',
    update_url='bbs:free_update',
    destroy_url='bbs:free_destroy',
    comment_url='bbs:free_comment',
    bookmark_url='bbs:free_bookmark',
)

freeUpdate = BoardUpdateView.as_view(
    model = models.FreeBoard,
    form_class= forms.FreeBoardCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="자유게시판 게시글 수정"
)

freeDestroy = BoardDestroyView.as_view(
    model=models.FreeBoard,
    redirect_url='bbs:free_list',

)

freeLike = LikeView.as_view(
    model = models.FreeBoard
)

freeDisLike = DisLikeView.as_view(
    model = models.FreeBoard
)

freeComment = CommentView.as_view(
    model = models.FreeBoard,
    form_class = forms.FreeBoardCommentForm,
    template_name="Comment.html",
)

freeBookMark = BookMarkView.as_view(
    model = models.FreeBoard
)
#일반시황분석
normalAnalysisList = BoardListView.as_view(
    model= models.NormalAnalysis,
    login_form = LoginForm ,
    success_url ='/analysis/',
    template_name = "Board_List.html",
    create_url = 'bbs:analysis_create',
    read_url='bbs:analysis_read',
    title="시황분석공유",
)

normalAnalysisCreate = BoardCreateView.as_view(
    model = models.NormalAnalysis,
    form_class = forms.NormalAnalysisCreationForm,
    template_name='Board_Create.html',
    title ="시황분석 게시글 작성"
)
normalAnalysisRead = BoardReadView.as_view(
    model = models.NormalAnalysis,
    comment_model = models.NormalAnalysisComment,
    comment_Form_class = forms.NormalAnalysisCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="시황분석공유",
    like_url='bbs:analysis_like',
    dislike_url='bbs:analysis_dislike',
    update_url='bbs:analysis_update',
    destroy_url= 'bbs:analysis_destroy',
    comment_url= 'bbs:analysis_comment',
)
normalAnalysisUpdate = BoardUpdateView.as_view(
    model = models.NormalAnalysis,
    form_class= forms.NormalAnalysisCreationForm,
    success_url = '/free/',
    template_name='Board_Create.html',
    title ="시황분석공유 게시글 수정",
)

normalAnalysisDestroy = BoardDestroyView.as_view(
    
)

normalAnalysisLike = LikeView.as_view(
    model = models.NormalAnalysis
)

normalAnalysisDisLike = DisLikeView.as_view(
    model = models.NormalAnalysis
)

normalAnalysisComment = CommentView.as_view(
    model = models.NormalAnalysis,
    form_class = forms.NormalAnalysisCommentForm,
    template_name="Comment.html",
)


#갤러리
galleryList = BoardListView.as_view(
    model= models.Gallery,
    login_form = LoginForm ,
    success_url ='/gallery/',
    template_name = "Board_List.html",
    create_url = 'bbs:gallery_create',
    read_url='bbs:gallery_read',
    title="갤러리",
)

galleryCreate = BoardCreateView.as_view(
    model = models.Gallery,
    form_class = forms.GalleryCreationForm,
    template_name='Board_Create.html',
    title ="갤러리 게시글 작성"
)
galleryRead = BoardReadView.as_view(
    model = models.Gallery,
    comment_model = models.GalleryComment,
    comment_Form_class = forms.GalleryCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="갤러리",
    like_url='bbs:gallery_like',
    dislike_url='bbs:gallery_dislike',
    update_url='bbs:gallery_update',
    destroy_url= 'bbs:gallery_destroy',
    comment_url= 'bbs:gallery_comment',
)
galleryUpdate = BoardUpdateView.as_view(
    model = models.Gallery,
    form_class= forms.GalleryCreationForm,
    success_url = '/gallery/',
    template_name='Board_Create.html',
    title ="갤러리 수정",
)

galleryDestroy = BoardDestroyView.as_view(
    
)

galleryLike = LikeView.as_view(
    model = models.Gallery
)

galleryDisLike = DisLikeView.as_view(
    model = models.Gallery
)

galleryComment = CommentView.as_view(
    model = models.Gallery,
    form_class = forms.GalleryCommentForm,
    template_name="Comment.html",
)

##################################################################################
#정보/꿀팁

honeyTipList = BoardListView.as_view(
    model= models.HoneyTip,
    login_form = LoginForm ,
    success_url ='/honeytip/',
    template_name = "Board_List.html",
    create_url = 'bbs:honeytip_create',
    read_url='bbs:honeytip_read',

    title="꿀팁 게시판",
)

honeyTipCreate = BoardCreateView.as_view(
    model = models.HoneyTip,
    form_class = forms.HoneyTipCreationForm,
    template_name='Board_Create.html',
    title ="꿀팁 작성"
)
honeyTipRead = BoardReadView.as_view(
    model = models.HoneyTip,
    comment_model = models.HoneyTipComment,
    comment_Form_class = forms.HoneyTipCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title ="꿀팁",
    like_url='bbs:honeytip_like',
    dislike_url='bbs:honeytip_dislike',
    update_url='bbs:honeytip_update',
    destroy_url= 'bbs:honeytip_destroy',
    comment_url= 'bbs:honeytip_comment',
)
honeyTipUpdate = BoardUpdateView.as_view(
    model = models.HoneyTip,
    form_class= forms.HoneyTipCreationForm,
    success_url = '/honeytip/',
    template_name='Board_Create.html',
    title ="꿀팁 수정",
)

honeyTipDestroy = BoardDestroyView.as_view(
    
)

honeyTipLike = LikeView.as_view(
    model = models.HoneyTip
)

honeyTipDisLike = DisLikeView.as_view(
    model = models.HoneyTip
)

honeyTipComment = CommentView.as_view(
    model = models.HoneyTip,
    form_class = forms.HoneyTipCommentForm,
    template_name="Comment.html",
)

####################################################################
#포럼
forumlist = ForumListView.as_view(
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Forum_List.html',
    title ="코인별 포럼"
)

#####################################################################
# 비트코인 포럼
forumBitCoinList = BoardListView.as_view(
    model= models.ForumBitCoin,
    login_form = LoginForm ,
    success_url ='/forum/bitcoin/',
    template_name = "Board_List.html",
    create_url = 'bbs:forumbitcoin_create',
    read_url='bbs:forumbitcoin_read',
    title="비트코인 포럼",
)

forumBitCoinCreate = BoardCreateView.as_view(
    model = models.ForumBitCoin,
    form_class = forms.ForumBitCoinCreationForm,
    template_name='Board_Create.html',
    title="비트코인 포럼",
)

forumBitCoinRead = BoardReadView.as_view(
    model = models.ForumBitCoin,
    comment_model = models.ForumBitCoinComment,
    comment_Form_class = forms.ForumBitCoinCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title="비트코인 포럼",
    like_url='bbs:forumbitcoin_like',
    dislike_url='bbs:forumbitcoin_dislike',
    update_url='bbs:forumbitcoin_update',
    destroy_url= 'bbs:forumbitcoin_destroy',
    comment_url= 'bbs:forumbitcoin_comment',
)

forumBitCoinUpdate = BoardUpdateView.as_view(
    model = models.ForumBitCoin,
    form_class= forms.ForumBitCoinCreationForm,
    success_url = '/forum/bitcoin/',
    template_name='Board_Create.html',
    title="비트코인 포럼",
)
forumBitCoinDestroy = BoardDestroyView.as_view(
    
)
forumBitCoinLike = LikeView.as_view(
    model = models.ForumBitCoin
)

forumBitCoinDisLike = DisLikeView.as_view(
    model = models.ForumBitCoin
)

forumBitCoinComment = CommentView.as_view(
    model = models.ForumBitCoin,
    form_class = forms.ForumBitCoinCommentForm,
    template_name="Comment.html",
)

#학회 게시판
societylist = ForumListView.as_view(
    form_class = LoginForm ,
    success_url = '/forum/',
    template_name='Society_List.html',
    title ="학회게시판"
)
#####################################################
#서울대학교

seoulUnvList = BoardListView.as_view(
    model= models.SeoulUnv,
    login_form = LoginForm ,
    success_url ='/forum/bitcoin/',
    template_name = "society_board_list.html",
    create_url = 'bbs:seoulunv_create',
    read_url='bbs:seoulunv_read',
    approval_url='bbs:seoulunv_approval_list',      #승인 url
    title="서울대 학회게시판",
    permission="A0",
    check_model= models.SeoulUnvSocietyRequest,
)

seoulUnvCreate = BoardCreateView.as_view(
    model = models.SeoulUnv,
    form_class = forms.SeoulUnvCreationForm,
    template_name='Board_Create.html',
    title="게시글 작성",
)

seoulUnvRead = BoardReadView.as_view(
    model = models.SeoulUnv,
    comment_model = models.SeoulUnvComment,
    comment_Form_class = forms.SeoulUnvCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title="서울대 학회",
    like_url='bbs:seoulunv_like',
    dislike_url='bbs:seoulunv_dislike',
    update_url='bbs:seoulunv_update',
    destroy_url= 'bbs:seoulunv_destroy',
    comment_url= 'bbs:seoulunv_comment',
)

seoulUnvUpdate = BoardUpdateView.as_view(
    model = models.SeoulUnv,
    form_class= forms.SeoulUnvCreationForm,
    success_url = '/forum/bitcoin/',
    template_name='Board_Create.html',
    title="게시글 수정",
)
seoulUnvDestroy = BoardDestroyView.as_view(
    
)
seoulUnvLike = LikeView.as_view(
    model = models.SeoulUnv
)

seoulUnvDisLike = DisLikeView.as_view(
    model = models.SeoulUnv
)

seoulUnvComment = CommentView.as_view(
    model = models.SeoulUnv,
    form_class = forms.SeoulUnvCommentForm,
    template_name="Comment.html",
)

#승인목록 ajax
seoulUnvApproval = SocietyApprovalView.as_view(
    model = models.SeoulUnvSocietyRequest,
    template_name="bbs/society_request_list.html",
    accept_url='bbs:seoulunv_approval_accept',
    reject_url='bbs:seoulunv_approval_reject',
    access_permission="A00" #승인목록 접근권한
)

#승인수락 ajax
seoulUnvAjaxAccept = SocietyAcceptView.as_view(
    model = models.SeoulUnvSocietyRequest,
    template_name = "bbs/society_request_list.html",
    accept_url='bbs:seoulunv_approval_accept',
    reject_url='bbs:seoulunv_approval_reject',
    access_permission='A00',                    #접근가능한 코드
    code="A0",                                  #승인후 변경될 코드
)

#승인거절 ajax
seoulUnvAjaxReject = SocietyRejectView.as_view(
    model = models.SeoulUnvSocietyRequest,
    template_name = "bbs/society_request_list.html",
    access_permission='A00',                       
    accept_url='bbs:seoulunv_approval_accept',
    reject_url='bbs:seoulunv_approval_reject',
)

#게시글 목록 ajax
seoulUnvAjaxList = SocietyApprovalView.as_view(
    model = models.SeoulUnv,
    template_name="bbs/society_board_list_ajax.html",
    access_permission="A0",
    read_url = 'bbs:seoulunv_read',
)

#권한요청
seoulUnvAjaxRequest = SocietyRequestView.as_view(
    model = models.SeoulUnvSocietyRequest,
    form = forms.SeoulUnvSocietyRequestForm,
    template_name="bbs/society_request_form_ajax.html"
)

seoulUnvAjaxClear = SocietyRequestView.as_view(
    model = models.SeoulUnvSocietyRequest,
    form = forms.SeoulUnvSocietyRequestForm,
    template_name="bbs/society_request_form_ajax.html"
)
###################################################
#제휴문의 생성
withCreate = BoardCreateView.as_view(
    model = models.With,
    form_class = forms.WithCreationForm,
    template_name='Board_Create.html',
    title="제휴문의",
)
#####################################################################
# 비트코인 포럼
usercolumnList = BoardListView.as_view(
    model= models.UserColumn,
    login_form = LoginForm ,
    success_url ='/forum/bitcoin/',
    template_name = "Board_List.html",
    create_url = 'bbs:usercolumn_create',
    read_url='bbs:usercolumn_read',
    title="유저칼럼",
)

usercolumnCreate = BoardCreateView.as_view(
    model = models.UserColumn,
    form_class = forms.UserColumnCreationForm,
    template_name='Board_Create.html',
    title="유저칼럼",
)

usercolumnRead = BoardReadView.as_view(
    model = models.UserColumn,
    comment_model = models.UserColumnComment,
    comment_Form_class = forms.UserColumnCommentForm,
    form_class = LoginForm,
    template_name='Board_Read.html',
    title="유저칼럼",
    like_url='bbs:usercolumn_like',
    dislike_url='bbs:usercolumn_dislike',
    update_url='bbs:usercolumn_update',
    destroy_url= 'bbs:usercolumn_destroy',
    comment_url= 'bbs:usercolumn_comment',
)

usercolumnUpdate = BoardUpdateView.as_view(
    model = models.UserColumn,
    form_class= forms.UserColumnCreationForm,
    success_url = '/forum/bitcoin/',
    template_name='Board_Create.html',
    title="유저칼럼",
)
usercolumnDestroy = BoardDestroyView.as_view(
    
)
usercolumnLike = LikeView.as_view(
    model = models.UserColumn
)

usercolumnDisLike = DisLikeView.as_view(
    model = models.UserColumn
)

usercolumnComment = CommentView.as_view(
    model = models.UserColumn,
    form_class = forms.UserColumnCommentForm,
    template_name="Comment.html",
)

###################################################
#제휴문의 생성
withCreate = BoardCreateView.as_view(
    model = models.With,
    form_class = forms.WithCreationForm,
    template_name='Board_Create.html',
    title="제휴문의",
)

###################################################
#게재중단 생성
suspendrequestCreate = BoardCreateView.as_view(
    model = models.SuspendRequest,
    form_class = forms.SuspendRequestCreationForm,
    template_name='Board_Create.html',
    title="게재중단 요청",
)

###################################################
# 성공 페이지
def sucessPage(request, select):
    context={'message':'','sub_message':''}

    #제휴문의
    if select ==1:
        context['message'] = '소중한 제안 감사드립니다.'
    elif select == 2:
        context['message'] = '소중한 신고 감사드립니다.'
        context['sub_message'] ='(단. 허위신고시 제재를 받을수 있습니다.)'
    return render(request, 'SucessPage.html', context)

###################################################
#호재 게시판 
def favorable(request):
    if request.method=="POST":
        pass
        
    search = request.GET.get('search', None) #검색
  
    favorable = models.Favorable.objects.all()
    form = LoginForm()
    if search:
        favorable = favorable.filter(
            Q(title__icontains=search) | Q(content__icontains=search) # Q 객체를 사용해서 검색한다. # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사 
            ).distinct() #중복을 제거한다.

    context= {
        'favorable':favorable,
        'form':form,
    }
    return render(request, 'Favorable.html',context)

#호재 좋아요
def favorableLike(request):
    post = get_object_or_404(models.Favorable, pk=request.POST.get('pk',None))
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)
    
    if not post_like_created:
        post_like.delete()
        message = "like_del"
    else:
        message = "like"
    context={
        'like_count':post.like_count,
        'message':message
    }
    return HttpResponse(json.dumps(context))

#공지사항
def noticeRead(request, pk):
    post = get_object_or_404(models.Notice, pk=pk)
    if post.author != request.user:
        post.views= post.views+1
        post.save()
    notice = models.Notice.objects.order_by('-id')[:3]
    context={
        'post':post,
        'notice':notice
    }
    return render(request,'Notice.html',context)

