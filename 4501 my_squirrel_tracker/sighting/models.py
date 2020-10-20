from django.db import models

# Create your models here.
class SquirrelCensusDatas(models.Model):

	Latitude = models.FloatField()
	Longitude = models.FloatField()
	Unique_Squirrel_ID = models.CharField(max_length=20)
	Shift = models.CharField(max_length=5)
	Date = models.CharField(max_length=10)
	Age = models.CharField(max_length=20)
	def __str__(self):
		return "%d" % self.pk