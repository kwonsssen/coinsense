from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

from django import forms
from . import models

class FreeBoardCreationForm(forms.ModelForm):
    class Meta:
        model = models.FreeBoard
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요')},)
        }

class FreeBoardCommentForm(forms.ModelForm):
    class Meta:
        model = models.FreeBoardComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
################################################################################################################################
# 시황분석폼
class NormalAnalysisCreationForm(forms.ModelForm):
    class Meta:
        model = models.NormalAnalysis
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class NormalAnalysisCommentForm(forms.ModelForm):
    class Meta:
        model = models.NormalAnalysisComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

################################################################################################################################
# 꿀팁 폼

class HoneyTipCreationForm(forms.ModelForm):
    class Meta:
        model = models.HoneyTip
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class HoneyTipCommentForm(forms.ModelForm):
    class Meta:
        model = models.HoneyTipComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

################################################################################################################################
# 비트포럼 폼
class ForumBitCoinCreationForm(forms.ModelForm):
    class Meta:
        model = models.ForumBitCoin
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class ForumBitCoinCommentForm(forms.ModelForm):
    class Meta:
        model = models.ForumBitCoinComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

################################################################################################################################
# 갤러리폼

class GalleryCreationForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = ['title','photo','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class GalleryCommentForm(forms.ModelForm):
    class Meta:
        model = models.GalleryComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
################################################################################################################################
# 유저컬럼폼

class UserColumnCreationForm(forms.ModelForm):
    class Meta:
        model = models.UserColumn
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class UserColumnCommentForm(forms.ModelForm):
    class Meta:
        model = models.UserColumnComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
        
################################################################################################################################
# 제휴문의 생성 폼
class WithCreationForm(forms.ModelForm):
    class Meta:
        model = models.With
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

################################################################################################################################
# 게재중단 생성 폼
class SuspendRequestCreationForm(forms.ModelForm):
    class Meta:
        model = models.SuspendRequest
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }


################################################################################################################################
# 서울대학교 폼

class SeoulUnvCreationForm(forms.ModelForm):
    class Meta:
        model = models.SeoulUnv
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class SeoulUnvCommentForm(forms.ModelForm):
    class Meta:
        model = models.SeoulUnvComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

class SeoulUnvSocietyRequestForm(forms.ModelForm):
    class Meta:
        model = models.SeoulUnvSocietyRequest
        fields = ['username','unv_number','department']


#호재요청
class FavorableRequestForm(forms.ModelForm):
    class Meta:
        model = models.FavorableRequest
        fields = ['content','date']