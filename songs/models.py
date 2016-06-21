from __future__ import unicode_literals

from django.db import models

# Create your models here.

class songModel(models.Model):
	title = models.CharField(max_length=200)
	rating = models.IntegerField()
	
	def __unicode__(self):
		return self.title
		
class genreModel(models.Model):
	name = models.CharField(max_length=30)
	songs = models.ManyToManyField(songModel)
	
	def __unicode__(self):
		return self.name


