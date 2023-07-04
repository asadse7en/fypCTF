from django.db import models
import hashlib
from django.db.models import Count

# Create your models here.

def get_upload_path(instance, filename) :
	return instance.category+'/challenges_{0}/{1}'.format(hashlib.md5(instance.name.encode('utf-8')).hexdigest(), filename)


class Challenges(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	challenge_id = models.CharField(max_length=300, primary_key=True)
	category = models.CharField(max_length=100)
	difficulty = models.CharField(max_length=100)
	description = models.CharField(max_length=2000, blank=True, default="")
	hints = models.CharField(max_length=500, blank=True, default="")
	points = models.IntegerField()
	flag = models.CharField(max_length=500)
	author_name = models.CharField(max_length=250)
	author_link = models.URLField(max_length=250, blank=True, default="")
	solve_count = models.IntegerField(default=0)



	@staticmethod
	def total_challenges():
		return Challenges.objects.count()

	@staticmethod
	def user_with_most_solves():
		most_solves = (
			ChallengesSolvedBy.objects
			.values('user_name')
			.annotate(solve_count=Count('user_name'))
			.order_by('-solve_count')
			.first()
		)
		if most_solves:
			return most_solves['user_name'], most_solves['solve_count']
		return None, None
	
	@staticmethod
	def user_with_least_solves():
		least_solves = (
			ChallengesSolvedBy.objects
			.values('user_name')
			.annotate(solve_count=Count('user_name'))
			.order_by('solve_count')
			.first()
		)
		if least_solves:
			return least_solves['user_name'], least_solves['solve_count']
		return None, None
	
	@staticmethod
	def challenge_with_most_solves():
		challenge = Challenges.objects.order_by('-solve_count').first()
		if challenge:
			return challenge.name, challenge.solve_count
		return None, None

	@staticmethod
	def challenge_with_least_solves():
		challenge = Challenges.objects.order_by('solve_count').first()
		if challenge:
			return challenge.name, challenge.solve_count
		return None, None


class ChallengesSolvedBy(models.Model) :
	name = models.CharField(max_length=250, unique=True)
	challenge_id =  models.CharField(max_length=250)
	user_name = models.CharField(max_length=250)
	points = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)
	first_blood = models.BooleanField(default=False)

	@staticmethod
	def most_first_blood():
		first_blood_count = ChallengesSolvedBy.objects.filter(first_blood=True).values('user_name').annotate(count=Count('user_name')).order_by('-count')

		if first_blood_count:
			most_first_blood_user = first_blood_count[0]['user_name']
			most_first_blood_count = first_blood_count[0]['count']
			return most_first_blood_user, most_first_blood_count

		return None, 0