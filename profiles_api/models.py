from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for user profile """
    def create_user(self, email, first_name, last_name, password=None):
        """ Create a new user profile """
        if not email:
            raise  ValueError("User must  have an email")

        email  = self.normailize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return User

    def create_superuser(email, first_name, last_name, password):
        """ Create super user with create_user function """
        user =  self.create_user(email,first_name,last_name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for user in the system """
    email =  models.EmailField(max_length = 255, unique = True)
    first_name =  models.CharField(max_length = 255)
    last_name =  models.CharField(max_length = 255)
    is_active =  models.BooleanField(default = True)
    is_staff =  models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD =  "email"
    REQUIRED_FIELD =  ["first_name", "last_name"]

    def get_full_name(self):
        """Retrive full name of the user """
        return self.name + self.last_name

    def get_short_name(self):
        """Retrive short name of the user """
        return self.name

    def _str_(self):
        """Return string representation  of a user """
        return self.email
