from django import forms
from django.contrib.auth import get_user_model
from .models import Profil, notify
from django.core.validators import RegexValidator
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Note

class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list': 'list__{}'.format(self._name)})

    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__{}">'.format(self._name)
        for item in self._list:
            data_list += '<option value="{}">{}</option>'.format(item[0], item[1])
        data_list += '</datalist>'

        return text_html + data_list

def get_user_list():
	user_list = get_user_model().objects.all()
	data_list =[]
	for user in user_list:
		data_list.append( (user.id,user))
	return data_list

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['receive_user', 'content']
		widgets={
			'receive_user':ListTextWidget(data_list=get_user_list() ,name="user_list")
		}
	def clean(self):
		print(self.cleaned_data)

class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['username','password']
        widgets = {
            'password':forms.PasswordInput(attrs={
				'class':'form-control',
				'placeholder':'Password'
				}),
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'ID'
				}),
		}

class UserCreationForm(forms.ModelForm):
	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'password',})
	)

	password2 = forms.CharField(
		label = 'Password Confirmation',
		widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'password',})
	)

	phone_num = forms.IntegerField( widget=forms.NumberInput(
		attrs = {
			'class' : 'form-control',
			'placeholder':'-없이 번호만 입력하세요.',
		})
	)

	address = forms.CharField(widget=forms.TextInput(
		attrs = {'class':'form-control','placeholder':'주소를입력해주세요.'}),
		required=False
	)

	email = forms.CharField(widget=
		forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'email@xxxxx.com',
			}))

	class Meta:
		model = get_user_model()
		fields = ['username','nickname','Photo','in_short']
		widgets = {
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'id'
				}),
			'nickname':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'닉네임을 입력해주세요.'
				}),
			'Photo':forms.FileInput(attrs={
				'class':'form-control',
				
				}),
			'in_short':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'한마디를 입력해주세요.'
				}),
		}
		
	def clean_username(self):
		username = self.cleaned_data.get('username', None)
		if username is None:
			raise forms.ValidationError("아이디를 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(username=username)
			if unique_test:
				raise forms.ValidationError("동일한 아이디가 존재합니다.")
		return username

	def clean_nickname(self):
		nickname = self.cleaned_data.get('nickname',None)
		if nickname is None:
			raise forms.ValidationError("닉네임을 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(nickname=nickname)
			if unique_test:
				raise forms.ValidationError("동일한 닉네임이 존재합니다.")
		return nickname

	def clean(self):
		email = self.cleaned_data.get("email",None)
		password = self.cleaned_data.get("password",None)
		password2 = self.cleaned_data.get("password2",None)
		password_isalpha = password[0].isalpha()
		
		if len(password) < 8:
			raise forms.ValidationError("비밀번호가 짧습니다. 최소 8글자 이상 입력해 주세요(영문+숫자)")
		if all(c.isalpha() == password_isalpha for c in password):
			raise forms.ValidationError("비밀번호는 영문과 숫자 조합으로 다시 입력해 주세요.")
		if password and password2 and password != password2:
			raise forms.ValidationError("두 비밀번호가 다릅니다.")
		
		if email is None:
			raise forms.ValidationError("이메일을 입력해주세요.")
		else:
			user_data= Profil.objects.all().filter(email=email)
			if user_data:
			 	raise forms.ValidationError("동일한 이메일이 존재합니다.")
		return self.cleaned_data

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
			email = self.cleaned_data['email']
			address = self.cleaned_data['address']
			phone_num = self.cleaned_data.get('phone_num',000)
			Profil.objects.create(user=user, email=email, address=address,phone_number=phone_num)
			
		return user

#정보 수정 폼
class UserUpdateForm(forms.ModelForm):
	

	address = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control'
		}), required=False,
	)

	phone_num= forms.CharField(validators=[RegexValidator(r'^010[1-9]\d{7}$')], max_length=11, widget= forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'01012345678'
        }),required=False,)

	email = forms.CharField(widget=forms.EmailInput(attrs={
		'class':'form-control',
		'placeholder':'email@xxxxx.com',
		}),required=False,)
	
	class Meta:
		model = get_user_model()
		fields = ['Photo','in_short']
		widgets = {
			'Photo':forms.FileInput(
				attrs={
				'class':'form-control',
				
			}),
			'in_short':forms.TextInput(
				attrs={
				'class':'form-control',
				},)
		}

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)

	def clean(self):
		return self.cleaned_data

	def save(self, commit=True):
		user = self.instance
		address = self.cleaned_data['address']
		email = self.cleaned_data['email']
		phone_num = self.cleaned_data['phone_num']
		photo = self.cleaned_data['Photo']
		in_short = self.cleaned_data['in_short']
		
		if photo:
			user.Photo = photo
		if in_short:
			user.in_short = in_short
		if email:
			user.user_of.email=email
		if address:
			user.user_of.address=address
		if phone_num:
			user.user_of.phone_number=phone_num
		print(user.in_short)
		if commit:
			user.user_of.save()
			user.save()
		return user

#admin전용
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ['username','nickname','level','exp','point', 'password', 'is_active', 'is_staff']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

#신고하기 폼
class NotifyForm(forms.ModelForm):
	class Meta:
		model = notify
		fields = ['content']
		widgets={
			'text': forms.Textarea(attrs={'class':"",'placeholder':'사유를 입력해 주세요',})
        		}