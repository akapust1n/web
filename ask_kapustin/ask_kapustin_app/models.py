
from django.db import models
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
	autor=models.ForeignKey(User)
	title = models.CharField(max_length=50)
	text = models.TextField()
	timeStamp = models.DateTimeField(default=datetime.datetime.now())
	rating=models.IntegerField()
	answerCount = models.IntegerField(default=0)


# Create your models here.
