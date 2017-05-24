from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class LocationMixin(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('location')
		widgets = {
			'location': forms.TextInput()
		}



class UserRegistrationForm(LocationMixin, UserCreationForm):
	first_name = forms.CharField(required=True, widget=forms.TextInput)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	username = forms.CharField()
	password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(required=True, label='Repeat Password', widget=forms.PasswordInput)
	location = forms.CharField(required=True, label='Location of interest')


	
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('passwords don\'t match.')
		return cd['password2']


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

