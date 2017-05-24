from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext

from .forms import LoginForm,UserForm, ProfileForm
from .models import Profile

# Create your views here.

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True

			return HttpResponse('success')

	else:
		user_form = UserForm()
		profile_form = ProfileForm()
	return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
	current_user = request.user

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Success')
				else :
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid account')
	else:
		form = LoginForm()
		print (current_user.id)
	return render(request, 'accounts/login.html', {'form': form})