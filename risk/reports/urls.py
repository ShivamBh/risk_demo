from django.conf.urls import url
from reports import views

urlpatterns = [
	url(r'^$', views.report_list_view, name="report_list"),
	url(r'^detail$', views.report_detail_view, name="report_detail"),
]