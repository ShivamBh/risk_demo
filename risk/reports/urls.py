from django.conf.urls import url
from .views import ReportDetail, ReportList

urlpatterns = [
	url(r'^$', ReportList.as_view(), name="report_list"),
	url(r'^(?P<pk>[0-9]+)/$', ReportDetail.as_view(), name="report_detail"),
]