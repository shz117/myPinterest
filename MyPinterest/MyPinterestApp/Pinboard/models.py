from django.db import models
from MyPinterest.MyPinterestApp import Picture
from MyPinterest.MyPinterestApp import User


class Board(models.Model):
    name = models.CharField()
    create_time = models.DateTimeField()
    owner = models.ForeignKey(User)

    ACCESS_PRIVATE = 0
    ACCESS_FRIENDS_ONLY = 1
    ACCESS_PUBLIC = 2
    ACCESS_TYPE = (
        (ACCESS_PRIVATE,'private'),
        (ACCESS_FRIENDS_ONLY,'friendsOnly'),
        (ACCESS_PUBLIC,'public')
    )
    access_level = models.CharField(max_length=1,
                                    choices=ACCESS_TYPE,
                                    default=ACCESS_PUBLIC)

class Pin(models.Model):
    to_board = models.ForeignKey(Board)
    picture = models.ForeignKey(Picture)
    from_pin = models.ForeignKey('self', null=True, blank=True, default=None, related_name='children')
    description = models.CharField()


