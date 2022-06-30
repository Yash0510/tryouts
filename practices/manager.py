from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UserCredentialsManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username
                                )
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email,
                                password=password,
                                username=username
                                )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user
