from django.db import models
from MyPinterest.MyPinterestApp.Pinboard.models import Board

class FollowStream(models.Model):
    name = models.CharField()
    boards = models.ManyToManyField(Board)


