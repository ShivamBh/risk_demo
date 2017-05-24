from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# class LocationMixin(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ('location',)
# 		widgets = {
# 			'location': forms.TextInput()
# 		}



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('location',)
	
	# def clean_password2(self):
	# 	cd = self.cleaned_data
	# 	if cd['password'] != cd['password2']:
	# 		raise forms.ValidationError('passwords don\'t match.')
	# 	return cd['password2']


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

