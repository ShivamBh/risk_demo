from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from .models import Report, ReportLoc

from accounts.models import Profile
# Create your views here.

# def report_list_view(request):
# 	current_user_loc = request.user.profile.get().location
# 	qs = Report.objects.filter(Q(location__icontains=current_user_loc))
# 	#latest_reports = Report.objects.all(Q(location__icontains=cure))
# 	template = 'reports/list.html'
# 	context = {"queryset": qs, "current_loc": current_user_loc}
# 	return render(request, template, context)

# def report_detail_view(request, id):
# 	report = get_object_or_404(Report, id=id)
# 	template = 'reports/detail.html'
# 	context = {"reports_list": report}
# 	return render(request, template, context)

class ReportList(ListView):
	model = Report

	# queryset = Report.objects.filter(Q(location__icontains='nepal'))
	context_object_name='reports'
	template_name = 'list.html'

	def get_queryset(self):
		user_loc = self.request.user.profile.get().location
		qs = super().get_queryset()
		return qs.filter(Q(location__icontains=user_loc))


class ReportDetail(DetailView):
	model = Report
	
	# loc_qs = loc.filter(id=id)
	# context_object_name = 'report'
	# template_name = 'reports/detail.html'
	# pk_url_kwarg = 'report_id'
	def get_context_data(self, *args, **kwargs):
		context = super(ReportDetail, self).get_context_data(*args, **kwargs)
		report_pk = self.kwargs.get("pk")
		loc = get_object_or_404(ReportLoc, pk=report_pk)
		context["lat"] = loc.latitude
		context["long"] = loc.longitude
		return context






	