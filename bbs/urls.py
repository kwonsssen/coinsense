from django.urls import path
from . import views

app_name='bbs'

#자유게시판 주소
urlpatterns = [
    path('free/', views.freeList, name="free_list"),
    path('free/create/', views.freeCreate , name="free_create"),
    path('free/<int:pk>/', views.freeRead , name="free_read"),
    path('free/edit/<int:pk>/', views.freeUpdate, name="free_update"),
    path('free/destroy/', views.freeDestroy, name="free_destroy"),
    path('free/like/', views.freeLike, name="free_like"),
    path('free/dislike/', views.freeDisLike, name="free_dislike"),
    path('free/comment/', views.freeComment, name="free_comment"), 
    path('free/bookmark/', views.freeBookMark, name="free_bookmark"),
]

#시황분석 게시판 주소
urlpatterns += [
    path('analysis/', views.normalAnalysisList, name="analysis_list"),                          #목록
    path('analysis/create/', views.normalAnalysisCreate , name="analysis_create"),              #쓰기
    path('analysis/<int:pk>/', views.normalAnalysisRead , name="analysis_read"),                #읽기
    path('analysis/edit/<int:pk>/', views.normalAnalysisUpdate, name="analysis_update"),        #수정
    path('analysis/destroy/', views.normalAnalysisDestroy, name="analysis_destroy"),   #삭제
    path('analysis/like/', views.normalAnalysisLike, name="analysis_like"),                     #추천
    path('analysis/dislike/', views.normalAnalysisDisLike, name="analysis_dislike"),            #비추천
    path('analysis/comment/', views.normalAnalysisComment, name="analysis_comment"),            #댓글
]

#꿀팁 게시판
urlpatterns += [
    path('honeytip/', views.honeyTipList, name="honeytip_list"),                          #목록
    path('honeytip/create/', views.honeyTipCreate , name="honeytip_create"),              #쓰기
    path('honeytip/<int:pk>/', views.honeyTipRead , name="honeytip_read"),                #읽기
    path('honeytip/edit/<int:pk>/', views.honeyTipUpdate, name="honeytip_update"),        #수정
    path('honeytip/destroy/', views.honeyTipDestroy, name="honeytip_destroy"),   #삭제
    path('honeytip/like/', views.honeyTipLike, name="honeytip_like"),                     #추천
    path('honeytip/dislike/', views.honeyTipDisLike, name="honeytip_dislike"),            #비추천
    path('honeytip/comment/', views.honeyTipComment, name="honeytip_comment"),            #댓글
]

#갤러리 게시판
urlpatterns += [
    path('gallery/', views.galleryList, name="gallery_list"),                          #목록
    path('gallery/create/', views.galleryCreate , name="gallery_create"),              #쓰기
    path('gallery/<int:pk>/', views.galleryRead , name="gallery_read"),                #읽기
    path('gallery/edit/<int:pk>/', views.galleryUpdate, name="gallery_update"),        #수정
    path('gallery/destroy/', views.galleryDestroy, name="gallery_destroy"),   #삭제
    path('gallery/like/', views.galleryLike, name="gallery_like"),                     #추천
    path('gallery/dislike/', views.galleryDisLike, name="gallery_dislike"),            #비추천
    path('gallery/comment/', views.galleryComment, name="gallery_comment"),            #댓글
]
#포럼게시판 주소
urlpatterns += [
    path('forum/', views.forumlist, name="forum_list"),
]

 #비트코인
urlpatterns += [
    path('forum/bitcoin/', views.forumBitCoinList, name="forumbitcoin_list"),                          #목록
    path('forum/bitcoin/create/', views.forumBitCoinCreate , name="forumbitcoin_create"),              #쓰기
    path('forum/bitcoin/<int:pk>/', views.forumBitCoinRead , name="forumbitcoin_read"),                #읽기
    path('forum/bitcoin/edit/<int:pk>/', views.forumBitCoinUpdate, name="forumbitcoin_update"),        #수정
    path('forum/bitcoin/destroy/', views.forumBitCoinDestroy, name="forumbitcoin_destroy"),   #삭제
    path('forum/bitcoin/like/', views.forumBitCoinLike, name="forumbitcoin_like"),                     #추천
    path('forum/bitcoin/dislike/', views.forumBitCoinDisLike, name="forumbitcoin_dislike"),            #비추천
    path('forum/bitcoin/comment/', views.forumBitCoinComment, name="forumbitcoin_comment"),            #댓글
]

 #유저컬럼
urlpatterns += [
    path('column/bitcoin/', views.usercolumnList, name="usercolumn_list"),                          #목록
    path('column/bitcoin/create/', views.usercolumnCreate , name="usercolumn_create"),              #쓰기
    path('column/bitcoin/<int:pk>/', views.usercolumnRead , name="usercolumn_read"),                #읽기
    path('column/bitcoin/edit/<int:pk>/', views.usercolumnUpdate, name="usercolumn_update"),        #수정
    path('column/bitcoin/destroy/', views.usercolumnDestroy, name="usercolumn_destroy"),   #삭제
    path('column/bitcoin/like/', views.usercolumnLike, name="usercolumn_like"),                     #추천
    path('column/bitcoin/dislike/', views.usercolumnDisLike, name="usercolumn_dislike"),            #비추천
    path('column/bitcoin/comment/', views.usercolumnComment, name="usercolumn_comment"),            #댓글
]


#학회 게시판 주소
urlpatterns += [
    path('society/', views.societylist, name="society_list"),
]
 #서울대학 학회 게시판
urlpatterns += [
    path('society/seoulunv/', views.seoulUnvList, name="seoulunv_list"),                            #목록
    path('society/seoulunv/create/', views.seoulUnvCreate , name="seoulunv_create"),                #쓰기
    path('society/seoulunv/<int:pk>/', views.seoulUnvRead , name="seoulunv_read"),                  #읽기
    path('society/seoulunv/edit/<int:pk>/', views.seoulUnvUpdate, name="seoulunv_update"),          #수정
    path('society/seoulunv/destroy/', views.seoulUnvDestroy, name="seoulunv_destroy"),     #삭제
    path('society/seoulunv/like/', views.seoulUnvLike, name="seoulunv_like"),                       #추천
    path('society/seoulunv/dislike/', views.seoulUnvDisLike, name="seoulunv_dislike"),              #비추천
    path('society/seoulunv/comment/', views.seoulUnvComment, name="seoulunv_comment"),              #댓글

    path('society/seoulunv/approval/', views.seoulUnvApproval, name="seoulunv_approval_list"),              #승인목록
    path('society/seoulunv/approval/accept', views.seoulUnvAjaxAccept, name="seoulunv_approval_accept"),      #승인허가
    path('society/seoulunv/approval/reject', views.seoulUnvAjaxReject, name="seoulunv_approval_reject"),      #승인허가
    path('society/seoulunv/list/', views.seoulUnvAjaxList, name="seoulunv_list_ajax"),                      #게시글목록ajaxseoulUnvAjaxList
    path('society/seoulunv/request/', views.seoulUnvAjaxRequest , name="seoulunv_request_ajax"),                      #게시글목록
    path('society/seoulunv/request/submit/', views.seoulUnvAjaxClear , name="seoulunv_request_ajax"),                      #게시글목록 ajaxseoulUnvAjaxList
    
]

#호재게시판
urlpatterns += [
    path('favorable/', views.favorable, name="favorable"),
    path('favorable/like/', views.favorableLike, name="favorable_like")
]


#하단 제휴/게재중단 요청
urlpatterns += [
    path('with/', views.withCreate, name="with_create"),
    path('sr/', views.suspendrequestCreate, name="sr_create"),
]


#공지사항
urlpatterns += [
    path('notice/<int:pk>', views.noticeRead, name="notice"),
]

#성공 여부 
urlpatterns += [
    path('sucess/<int:select>/', views.sucessPage, name='succes_page')
]
