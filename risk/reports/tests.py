from django.test import TestCase
from reports.models import Report

# Create your tests here.
class ReportTests(TestCase):

	def test_str(self):
		my_title = Report(title="Basic Title for test")
		self.assertEquals(str(my_title), "Basic Title for test")
		

