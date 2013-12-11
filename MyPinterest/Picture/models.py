from django.db import models
from MyPinterest import settings
from MyPinterest.User.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

class Picture(models.Model):
    first_piner = models.ForeignKey(User,related_name='first_piner')
    web_url = models.URLField(null=True, blank=True)
    image = models.FileField(upload_to='pictures/')
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    liked_by_users = models.ManyToManyField(User,'liker')