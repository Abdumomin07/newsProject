from django.db import models

# Create your models here.
class Post(models.Model):
	# author = models.CharField(max_length=100)
	title = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.title

