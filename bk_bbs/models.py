from django.db import models
from django.contrib.auth import get_user_model
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.urls import reverse



###############################################################################################################################
#  시황분석 모델들
class MarketBoard(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='MBlike_user_set',
                                           through='MarketBoardLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='MBdislike_user_set',
                                           through='MarketBoardDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:market_read', args=[self.id])

    def get_board_name(self):
        return "판매 게시판"

class MarketBoardComment(models.Model):
    post = models.ForeignKey(MarketBoard, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class MarketBoardLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(MarketBoard, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MarketBoardDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(MarketBoard, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# 이벤트 모델
class Event(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Elike_user_set',
                                           through='EventLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Edislike_user_set',
                                           through='EventDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:event_read', args=[self.id])

    def get_board_name(self):
        return "이벤트 게시판"

class EventComment(models.Model):
    post = models.ForeignKey(Event, verbose_name="event", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class EventLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Event, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EventDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# 코인분석 모델
class CoinAnalysis(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='CAike_user_set',
                                           through='CoinAnalysisLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='CAislike_user_set',
                                           through='CoinAnalysisDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:coinanalysis_read', args=[self.id])

    def get_board_name(self):
        return "코인분석 게시판"

class CoinAnalysisComment(models.Model):
    post = models.ForeignKey(CoinAnalysis, verbose_name="CoinAnalysis", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class CoinAnalysisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(CoinAnalysis, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CoinAnalysisDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(CoinAnalysis, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# 시황분석 모델
class Analysis(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Aike_user_set',
                                           through='AnalysisLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Aislike_user_set',
                                           through='AnalysisDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:analysis_read', args=[self.id])

    def get_board_name(self):
        return "시황분석 게시판"

class AnalysisComment(models.Model):
    post = models.ForeignKey(Analysis, verbose_name="Analysis", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class AnalysisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Analysis, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AnalysisDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Analysis, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#############################################################################################
# 동영상 컨텐츠 모델
class Video(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Vike_user_set',
                                           through='VideoLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Vislike_user_set',
                                           through='VideoDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:video_read', args=[self.id])

    def get_board_name(self):
        return "동영상 게시판"

class VideoComment(models.Model):
    post = models.ForeignKey(Video, verbose_name="Video", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class VideoLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Video, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VideoDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# 뉴스모델
class News(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Nike_user_set',
                                           through='NewsLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Nislike_user_set',
                                           through='NewsDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:news_read', args=[self.id])

    def get_board_name(self):
        return "뉴스 게시판"

class NewsComment(models.Model):
    post = models.ForeignKey(News, verbose_name="News", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class NewsLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NewsDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#############################################################################################
# ico
class ICORating(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Iike_user_set',
                                           through='ICORatingLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Iislike_user_set',
                                           through='ICORatingDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:icoRating_read', args=[self.id])

    def get_board_name(self):
        return "ICO"

class ICORatingComment(models.Model):
    post = models.ForeignKey(ICORating, verbose_name="ICORating", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ICORatingBkComment(models.Model):
    comment = models.ForeignKey(ICORatingComment, verbose_name="ico comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ICORatingLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ICORating, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ICORatingDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ICORating, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

##
#ico bk의견
class BKICORating(summer_model.Attachment):
    ico = models.ForeignKey(ICORating ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='bkIcolike_user_set',
                                           through='BKICORatingLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='bkIcodislike_user_set',
                                           through='BKICORatingDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bk:icoRating_read', args=[self.ico.id])

    def get_board_name(self):
        return "ICO BK 게시판"

class BKICORatingLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(BKICORating, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BKICORatingDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(BKICORating, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

##
#ico 컬럼의견
class ColumBKICORating(summer_model.Attachment):
    ico = models.ForeignKey(ICORating ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='colbkIcolike_user_set',
                                           through='ColumBKICORatingLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='colbkIcodislike_user_set',
                                           through='ColumBKICORatingDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()
        
    def get_absolute_url(self):
        return reverse('bk:icoRating_read', args=[self.ico.id])
        
class ColumBKICORatingLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ColumBKICORating, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ColumBKICORatingDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ColumBKICORating, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
