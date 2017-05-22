from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Report

# Create your views here.

def report_list_view(request):
	latest_reports = Report.objects.all()
	template = 'reports/index.html'
	context = {"latest_reports": latest_reports}
	return render(request, template, context)

def report_detail_view(request):
	reports_list = Report.objects.all()
	template = 'reports/detail.html'
	context = {"reports_list": reports_list}
	return render(request, template, context)