from django.db import models
from MyPinterest.Pinboard.models import Board
from MyPinterest.User.models import User


class FollowStream(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)
    boards = models.ManyToManyField(Board)

class FriendStatus(models.Model):
    from_user = models.ForeignKey(User,related_name='from_user')
    to_user= models.ForeignKey(User,related_name='to_user')

    STATUS_REQUEST = 0
    STATUS_ACCEPT = 1
    STATUS_REJECT = 2
    STATUS_TYPE = (
        (STATUS_REQUEST,'requested'),
        (STATUS_ACCEPT,'accepted'),
        (STATUS_REJECT,'rejected')
    )
    status = models.CharField(max_length=1,
                                    choices=STATUS_TYPE,
                                    default=STATUS_REQUEST)
    class Meta:
        unique_together = (("from_user", "to_user"),)


