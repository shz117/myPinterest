from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from MyPinterest.MyPinterestApp.Pinboard.models import Board


class UserManager(BaseUserManager):
    def create_user(self, email, name, createTime, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            createTime=createTime
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #def create_superuser(self, email, name, phone, address, company, role, createTime, password):
    #    if not email:
    #        raise ValueError('Users must have an email address')
    #
    #    if not password:
    #        raise ValueError('Users must have a password')
    #
    #    user = self.model(
    #        email=self.normalize_email(email),
    #        name=name,
    #        phone=phone,
    #        address=address,
    #        company=company,
    #        role=role,
    #        createTime=createTime
    #    )
    #
    #    user.is_admin = True
    #    user.set_password(password)
    #    user.save(using=self._db)
    #    return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=16)
    email = models.EmailField(max_length=255, unique=True, db_index=True,)
    boards = models.ManyToManyField(Board)
    createTime = models.DateTimeField()
    lastLoginTime = models.DateTimeField(blank=True, null=True)
    lastLoginIP = models.IPAddressField(blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  # access admin pages

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'createTime']

    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return unicode(self.name)

    def get_full_name(self):
        return unicode(self.name)

    def get_short_name(self):
        return unicode(self.name)

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True