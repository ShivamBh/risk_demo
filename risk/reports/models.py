from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Report(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=100)
	# slug = models.SlugField(unique=True)
	category = models.CharField(max_length=100, blank=False, null=False)
	description = models.TextField()
	advice = models.TextField()


	def __str__(self):
		return self.title

	def get_absolute_url(self, id):
		return reverse("reports:report_detail", kwargs={"id":self.id})

class ReportLoc(models.Model):
	report = models.OneToOneField(Report)
	latitude = models.DecimalField(max_digits=8, decimal_places=4)
	longitude = models.DecimalField(max_digits=8, decimal_places=4)

	def __str__(self):
		return self.report.title


		