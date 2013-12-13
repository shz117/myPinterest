from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
#from Pinboard.models import Board


class UserManager(BaseUserManager):
    def create_user(self, email, name, createTime, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=name,
            createTime=createTime
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=16,unique=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True,)
    #boards = models.ManyToManyField(Board)
    createTime = models.DateTimeField()
    lastLoginTime = models.DateTimeField(blank=True, null=True)
    lastLoginIP = models.IPAddressField(blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  # access admin pages

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'createTime']

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return unicode(self.username)

    def get_full_name(self):
        return unicode(self.username)

    def get_short_name(self):
        return unicode(self.username)

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True