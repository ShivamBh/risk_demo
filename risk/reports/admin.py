from django.contrib import admin
from reports.models import Report, ReportLoc
# Register your models here.

class ReportAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'location')


admin.site.register(Report, ReportAdmin)
admin.site.register(ReportLoc)
