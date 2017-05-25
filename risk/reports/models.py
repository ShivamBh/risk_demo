from django.db import models


# Create your models here.
class Report(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=100)

	category = models.CharField(max_length=100, blank=False, null=False)
	description = models.TextField()
	advice = models.TextField()


	def __str__(self):
		return self.title

class ReportLoc(models.Model):
	report = models.OneToOneField(Report)
	latitude = models.DecimalField(max_digits=5, decimal_places=4)
	longitude = models.DecimalField(max_digits=5, decimal_places=4)

	def __str__(self):
		return self.report.title


		