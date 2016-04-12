
from django.db import models


class Question(models.Model):
	# author = models.ForeignKey(Profile, null=True)
	title = models.CharField(max_length=50)
	text = models.TextField()
	timeStamp = models.DateTimeField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	# hashtags = models.ManyToManyField(Hashtag)
	answerCount = models.IntegerField(default=0)


# Create your models here.
