from django.contrib import admin
from reports.models import Report
# Register your models here.

class ReportAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'location')


admin.site.register(Report, ReportAdmin)
