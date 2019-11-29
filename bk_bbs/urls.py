from django.urls import path
from . import views
app_name='bk'

#판매게시판
urlpatterns = [
    path('market/', views.marketBoardList, name="market_list"),                          #목록
    path('market/create/', views.marketBoardCreate , name="market_create"),              #쓰기
    path('market/<int:pk>/', views.marketBoardRead , name="market_read"),                #읽기
    path('market/edit/<int:pk>/', views.marketBoardUpdate, name="market_update"),        #수정
    path('market/destroy/<int:pk>/', views.marketBoardDestroy, name="market_destroy"),   #삭제
    path('market/like/', views.marketBoardLike, name="market_like"),                     #추천
    path('market/dislike/', views.marketBoardDisLike, name="market_dislike"),            #비추천
    path('market/comment/', views.marketBoardComment, name="market_comment"),            #댓글
]

#이벤트 게시판
urlpatterns += [
    path('event/', views.eventList, name="event_list"),                          #목록
    path('event/create/', views.eventCreate , name="event_create"),              #쓰기
    path('event/<int:pk>/', views.eventRead , name="event_read"),                #읽기
    path('event/edit/<int:pk>/', views.eventUpdate, name="event_update"),        #수정
    path('event/destroy/<int:pk>/', views.eventDestroy, name="event_destroy"),   #삭제
    path('event/like/', views.eventLike, name="event_like"),                     #추천
    path('event/dislike/', views.eventDisLike, name="event_dislike"),            #비추천
    path('event/comment/', views.eventComment, name="event_comment"),            #댓글
]

#코인분석 게시판
urlpatterns += [
    path('coinanalysis/', views.coinAnalysisList, name="coinanalysis_list"),                          #목록
    path('coinanalysis/create/', views.coinAnalysisCreate , name="coinanalysis_create"),              #쓰기
    path('coinanalysis/<int:pk>/', views.coinAnalysisRead , name="coinanalysis_read"),                #읽기
    path('coinanalysis/edit/<int:pk>/', views.coinAnalysisUpdate, name="coinanalysis_update"),        #수정
    path('coinanalysis/destroy/<int:pk>/', views.coinAnalysisDestroy, name="coinanalysis_destroy"),   #삭제
    path('coinanalysis/like/', views.coinAnalysisLike, name="coinanalysis_like"),                     #추천
    path('coinanalysis/dislike/', views.coinAnalysisDisLike, name="coinanalysis_dislike"),            #비추천
    path('coinanalysis/comment/', views.coinAnalysisComment, name="coinanalysis_comment"),            #댓글
]

#시황분석 게시판
urlpatterns += [
    path('analysis/', views.analysisList, name="analysis_list"),                          #목록
    path('analysis/create/', views.analysisCreate , name="analysis_create"),              #쓰기
    path('analysis/<int:pk>/', views.analysisRead , name="analysis_read"),                #읽기
    path('analysis/edit/<int:pk>/', views.analysisUpdate, name="analysis_update"),        #수정
    path('analysis/destroy/<int:pk>/', views.analysisDestroy, name="analysis_destroy"),   #삭제
    path('analysis/like/', views.analysisLike, name="analysis_like"),                     #추천
    path('analysis/dislike/', views.analysisDisLike, name="analysis_dislike"),            #비추천
    path('analysis/comment/', views.analysisComment, name="analysis_comment"),            #댓글
]

#동영상 컨텐츠 게시판
urlpatterns += [
    path('video/', views.videoList, name="video_list"),                          #목록
    path('video/create/', views.videoCreate , name="video_create"),              #쓰기
    path('video/<int:pk>/', views.videoRead , name="video_read"),                #읽기
    path('video/edit/<int:pk>/', views.videoUpdate, name="video_update"),        #수정
    path('video/destroy/<int:pk>/', views.videoDestroy, name="video_destroy"),   #삭제
    path('video/like/', views.videoLike, name="video_like"),                     #추천
    path('video/dislike/', views.videoDisLike, name="video_dislike"),            #비추천
    path('video/comment/', views.videoComment, name="video_comment"),            #댓글
]

#뉴스 게시판
urlpatterns += [
    path('news/', views.newsList, name="news_list"),                          #목록
    path('news/create/', views.newsCreate , name="news_create"),              #쓰기
    path('news/<int:pk>/', views.newsRead , name="news_read"),                #읽기
    path('news/edit/<int:pk>/', views.newsUpdate, name="news_update"),        #수정
    path('news/destroy/<int:pk>/', views.newsDestroy, name="news_destroy"),   #삭제
    path('news/like/', views.newsLike, name="news_like"),                     #추천
    path('news/dislike/', views.newsDisLike, name="news_dislike"),            #비추천
    path('news/comment/', views.newsComment, name="news_comment"),            #댓글
]

#ICO_RATING
urlpatterns += [
    path('icoRating/', views.icoRatingList, name="icoRating_list"),                          #목록
    path('icoRating/create/', views.icoRatingCreate , name="icoRating_create"),              #쓰기
    path('icoRating/<int:pk>/', views.icoRatingRead , name="icoRating_read"),                #읽기
    path('icoRating/edit/<int:pk>/', views.icoRatingUpdate, name="icoRating_update"),        #수정
    path('icoRating/destroy/<int:pk>/', views.icoRatingDestroy, name="icoRating_destroy"),   #삭제
    path('icoRating/like/', views.icoRatingLike, name="icoRating_like"),                     #추천
    path('icoRating/dislike/', views.icoRatingDisLike, name="icoRating_dislike"),            #비추천
    path('icoRating/comment/<int:pk>/', views.icoRatingComment, name="icoRating_comment"),    #댓글

    path('icoRating/bkopinion/<int:pk>/',views.bkIcoReadAjax , name="bk_ico_read"),                     #bk ajax 읽기
    path('icoRating/bkopinion/create/<int:pk>/', views.bkicoCreate, name="bk_ico_create"),              #bk 게시글 작성
    path('icoRating/bkopinion/edit/<int:pk>/', views.bkicoUpdate, name="bk_ico_update"),                #bk 게시글 수정
    path('icoRating/bkopinion/like/', views.bkIcoRatingLike, name="bk_icoRating_like"),                 #추천
    path('icoRating/bkopinion/dislike/', views.bkIcoRatingDisLike, name="bk_icoRating_dislike"),        #비추천
    
    path('icoRating/colum/<int:pk>/',views.columRead , name="colum_ico_read"),                           #colum 읽기
    path('icoRating/colum/create/<int:pk>/', views.columIcoCreate, name="colum_ico_create"),             #colum 생성
    path('icoRating/colum/edit/<int:pk>/', views.columIcoUpdate, name="colum_ico_update"),               #colum 수정
    path('icoRating/colum/like/', views.columIcoRatingLike, name="colum_icoRating_like"),                #colum 추천
    path('icoRating/colum/dislike/', views.columIcoRatingDisLike, name="colum_icoRating_dislike"),       #colum 비추천

    
]