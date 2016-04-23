from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    text = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now())
    rating = models.IntegerField()
    answerCount = models.IntegerField(default=0)

# Create your models here.
