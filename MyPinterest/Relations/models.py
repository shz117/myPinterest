from django.db import models
from MyPinterest.Pinboard.models import Board
from MyPinterest.User.models import User


class FollowStream(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)
    boards = models.ManyToManyField(Board)


