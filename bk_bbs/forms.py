from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

from django import forms
from . import models

class MarketBoardCreationForm(forms.ModelForm):
    class Meta:
        model = models.MarketBoard
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class MarketBoardCommentForm(forms.ModelForm):
    class Meta:
        model = models.MarketBoardComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
###############################################################################
# 이벤트
class EventCreationForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class EventCommentForm(forms.ModelForm):
    class Meta:
        model = models.EventComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

###############################################################################
# CoinAnalysis 폼
class CoinAnalysisCreationForm(forms.ModelForm):
    class Meta:
        model = models.CoinAnalysis
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class CoinAnalysisCommentForm(forms.ModelForm):
    class Meta:
        model = models.CoinAnalysisComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
###############################################################################
# 시황분석폼
class AnalysisCreationForm(forms.ModelForm):
    class Meta:
        model = models.Analysis
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class AnalysisCommentForm(forms.ModelForm):
    class Meta:
        model = models.AnalysisComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }
###############################################################################
# 동영상폼
class VideoCreationForm(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = models.VideoComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

###############################################################################
# 뉴스폼
class NewsCreationForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = models.NewsComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }


###############################################################################
# ICO Rating 폼
class ICORatingCreationForm(forms.ModelForm):
    class Meta:
        model = models.ICORating
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

class ICORatingCommentForm(forms.ModelForm):
    class Meta:
        model = models.ICORatingComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

class ICORatingBkCommentForm(forms.ModelForm):
    class Meta:
        model = models.ICORatingBkComment
        fields = ['text']
        widgets={
        'text': forms.TextInput(attrs={
        'class':"form-controlcomment-Table",
        'style':'width:670px;height:40px;margin-right:10px;',
        'placeholder':'댓글을 입력해주세요.',
            })
        }

#BK ICO 폼
class BKICORatingCreationForm(forms.ModelForm):
    class Meta:
        model = models.BKICORating
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

#컬럼 ICO 폼
class ColumICORatingCreationForm(forms.ModelForm):
    class Meta:
        model = models.ColumBKICORating
        fields = ['title','summer_field']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요 (최대 : 30자)','class':'input_first_title'}),
            'summer_field' :summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
        }

