from django.db import models
from django.contrib.auth import get_user_model
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields
from django.urls import reverse

# Create your models here.
class FreeBoard(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='like_user_set',
                                           through='Like') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='dislike_user_set',
                                           through='DisLike') # post.like_set 으로 접근 가능
    bookmark_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='bookmark_user_set',
                                           through='BookMark') # post.like_set 으로 접근 가능
                                        

    def __str__(self):
        return self.title

    def get_code(self):
        return 'Z0'

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:free_read', args=[self.id])
    
    def get_board_name(self):
        return "자유게시판"

class FreeBoardComment(models.Model):
    post = models.ForeignKey(FreeBoard, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(FreeBoard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(FreeBoard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookMark(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bookamrk_set')
    post = models.ForeignKey(FreeBoard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

###############################################################################################################################
#  시황분석 모델들
class NormalAnalysis(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='NAlike_user_set',
                                           through='NormalAnalysisLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='NAdislike_user_set',
                                           through='NormalAnalysisDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:analysis_read', args=[self.id])

    def get_board_name(self):
        return "시황분석게시판"

class NormalAnalysisComment(models.Model):
    post = models.ForeignKey(NormalAnalysis, verbose_name="Free Board", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class NormalAnalysisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(NormalAnalysis, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NormalAnalysisDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(NormalAnalysis, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


###############################################################################################################################
#  꿀팁(Honey-Tip) 모델들
class HoneyTip(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='HTlike_user_set',
                                           through='HoneyTipLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='HTdislike_user_set',
                                           through='HoneyTipDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:honeytip_read', args=[self.id])
   
    def get_board_name(self):
        return "꿀팁 게시판"

class HoneyTipComment(models.Model):
    post = models.ForeignKey(HoneyTip, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class HoneyTipLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(HoneyTip, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HoneyTipDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(HoneyTip, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



###############################################################################################################################
#  ForumBitCoin
class ForumBitCoin(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='FBClike_user_set',
                                           through='ForumBitCoinLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='FBCdislike_user_set',
                                           through='ForumBitCoinDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:forumbitcoin_read', args=[self.id])

    def get_board_name(self):
        return "포럼-비트코인 게시판"

class ForumBitCoinComment(models.Model):
    post = models.ForeignKey(ForumBitCoin, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class ForumBitCoinLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ForumBitCoin, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ForumBitCoinDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(ForumBitCoin, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#######################################################################################################################################
#호재
class Favorable(models.Model):
    title = models.CharField(verbose_name="title",max_length=20)
    content = models.CharField(verbose_name="content",max_length=20)
    photo = models.ImageField(blank=True)
    date = models.DateTimeField()
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Favorable_like_user_set',
                                           through='Favorable_Like') # post.like_set 으로 접근 가능
    @property
    def like_count(self):
        return self.like_user_set.count()

    def __str__(self):
        return self.title

class Favorable_Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Favorable, on_delete=models.CASCADE , related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)    #필수요소
    updated_at = models.DateTimeField(auto_now=True)        #필수요소

class FavorableRequest(models.Model):
    content = models.CharField(verbose_name="제보내용",max_length=20)
    date = models.DateTimeField('날짜')

###############################################################################################################################
#  ForumBitCoin
class Gallery(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    #사진
    photo = models.ImageField(
        verbose_name='gallery photo',
        upload_to="gallery/%Y/%m/%d",
        blank=True,
        null=True,
    )
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='Glike_user_set',
                                           through='galleryLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='GCdislike_user_set',
                                           through='galleryDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:gallery_read', args=[self.id])

    def get_board_name(self):
        return "갤러리"

class GalleryComment(models.Model):
    post = models.ForeignKey(Gallery, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class GalleryLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GalleryDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


###############################################################################################################################
#  유저 칼럼
class UserColumn(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='UClike_user_set',
                                           through='UserColumnLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='UCdislike_user_set',
                                           through='UserColumnDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:usercolumn_read', args=[self.id])

    def get_board_name(self):
        return "유저 칼럼"
        
class UserColumnComment(models.Model):
    post = models.ForeignKey(UserColumn, verbose_name="Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class UserColumnLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(UserColumn, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserColumnDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(UserColumn, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

###############################################################################################################################
#  제휴문의 
class With(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def get_absolute_url(self):
        return reverse('bbs:succes_page', args=[1])


###############################################################################################################################
#  게재중단요청 
class SuspendRequest(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def get_absolute_url(self):
        return reverse('bbs:succes_page', args=[2])

#공지사항
class Notice(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bbs:notice', args=[self.id])
###############################################################################################################################
#  ForumBitCoin
class SeoulUnv(summer_model.Attachment):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss')
    title = models.CharField(verbose_name="title",max_length=40)
    summer_field = summer_fields.SummernoteTextField(default='')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    views = models.IntegerField(null=False, blank=False, default=0) #조회수
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='snuvClike_user_set',
                                           through='SeoulUnvLike') # post.like_set 으로 접근 가능
    dislike_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='sunvdislike_user_set',
                                           through='SeoulUnvDisLike') # post.like_set 으로 접근 가능

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.like_user_set.count()
        
    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def get_absolute_url(self):
        return reverse('bbs:seoulunv_read', args=[self.id])
    
    @property
    def get_code(self):
        return 'A00'

    def get_board_name(self):
        return "서울학회 게시판"
        
class SeoulUnvComment(models.Model):
    post = models.ForeignKey(SeoulUnv, verbose_name="HoneyTip Comment", on_delete=models.CASCADE,  related_name='%(app_label)s_%(class)ss') 
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class SeoulUnvLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(SeoulUnv, on_delete=models.CASCADE ,related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SeoulUnvDisLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(SeoulUnv, on_delete=models.CASCADE, related_name='dislike_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

### 학회승인요청목록
class SeoulUnvSocietyRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    username = models.CharField('이름',max_length=30)
    unv_number = models.IntegerField('학번')
    department = models.CharField('학과',max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
