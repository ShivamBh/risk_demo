from django import forms 
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
	location = forms.CharField(label='Location of interest')

	class Meta:
		model = Profile
		fields = ('username', 'first_name', 'last_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('passwords don\'t match.')
		return cd['password2']


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

