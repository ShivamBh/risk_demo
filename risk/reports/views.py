from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Report

from accounts.models import Profile
# Create your views here.

def report_list_view(request):
	current_user_loc = request.user.profile.get()
	
	latest_reports = Report.objects.all()
	template = 'reports/list.html'
	context = {"latest_reports": latest_reports, "current_loc": current_user_loc}
	return render(request, template, context)

def report_detail_view(request):
	reports_list = Report.objects.all()
	template = 'reports/detail.html'
	context = {"reports_list": reports_list}
	return render(request, template, context)