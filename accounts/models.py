from django.db import models

# Create your models here.

class Teams(models.Model) :
	first_name = models.CharField(max_length=50, default="lastname")
	last_name = models.CharField(max_length=50, default="lastname")
	teamname = models.CharField(max_length=250, primary_key=True)
	affiliation = models.CharField(max_length=500, blank=True)
	email = models.EmailField(max_length=250, unique=True)
	points = models.IntegerField(default=0)

	@staticmethod
	def total_participants():
		return Teams.objects.count()