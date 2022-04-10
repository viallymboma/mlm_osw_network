from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.utils import timezone
import datetime

from django.contrib.auth.models import User

import os
from pickle import FALSE


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

POSITION = (
    ("Left", "Left"),
    ("right", "right"),
)


USER_TYPE = (
    ("IBA", "IBA"),
    ("Customer", "Customer"),
)


COUNTRY = (
    ("Ghana", "Ghana"),
    ("Nigeria", "Nigeria"),
    ("Cameroon", "Cameroon"),
    ("Ivory Coast", "Ivory Coast"),
    ("Togo", "Togo"),
)

# Create your models here.

class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='Customer')

class IBAManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='IBA')


class SubadminTable(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="user")
    admin_password = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(max_length=1000, choices=COUNTRY, blank=False, null=False)

    # date_created = models.DateTimeField(auto_now_add = True, auto_now = False, default="March 25, 2022, 1:47 p.m")
    # date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)
    # objects = UserManager()

    # def get_full_name(self):
    #     """ Return the first_name plus the last_name, with a space in between. """
    #     full_name = "%s %s" % (self.first_name, self.last_name)
    #     return full_name.strip()
    
    def __str__(self):
        return self.username


class ClientsTable(models.Model):

    # def upload_photo(instance, filename):
    #     ext = os.path.splitext(filename)
    #     return "photos/{username}.jpg".format(
    #         member_id=instance.username, file_ext=str(ext).lower()
    #     )

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)

    my_subadmin = models.ForeignKey(SubadminTable, null=False, blank=False, on_delete=models.CASCADE, related_name="mysubadmin")
    subadmin_password = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
    admin_password = models.CharField(max_length=255, blank=True, null=True)

    sponsortID = models.CharField(max_length=255, blank=True, null=True)
    uplinerID = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=1000, choices=USER_TYPE, default="IBA", blank=False, null=False)

    # my position on the network
    my_position = models.CharField(max_length=1000, choices=POSITION, default="Left", blank=False, null=False)
    my_left_child = models.CharField(max_length=1000, choices=POSITION, default="Left", blank=False, null=False)
    my_right_child = models.CharField(max_length=1000, choices=POSITION, default="Left", blank=False, null=False)

    # my other details 
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField(blank=True, null=True, default=0, help_text="Personal Phone")
    tel_fixe = models.IntegerField(blank=True, null=True, default=0, help_text="Fixed Line")
    address = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=1000, choices=COUNTRY, blank=False, null=False)
    national_id_card_number = models.CharField(max_length=255, blank=True, null=True)

    # Bank details
    bank_name = models.CharField(max_length=20, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=20, blank=True, null=True)
    account_name = models.CharField(max_length=20, blank=True, null=True)
    account_number = models.IntegerField(blank=True, null=True, default=0, help_text="Personal Phone")

    # personal_volume = 

    date_created = models.DateTimeField(auto_now_add = True, auto_now = False)
    date_updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    clients = models.Manager()
    # ClientsTable.clients.all()
    customers = CustomerManager()
    # ClientsTable.customers.all()
    ibas = IBAManager()
    # ClientsTable.ibas.all()

    def get_full_name(self):
        """ Return the first_name plus the last_name, with a space in between. """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.username







# class SubAdminManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(role='A')
#     # def create_user(self, username, password=None, **extra_fields):
#     #     """Creates and saves a new user"""
#     #     if not username:
#     #         raise ValueError("username address required")
#     #     user = self.model(username=username)
#     #     user.set_password(password)
#     #     user.save(using=self._db)

#     #     return user

#     # def create_superuser(self, username, password):
#     #     """Create and save a new super user"""
#     #     user = self.create_user(username, password)
#     #     user.is_staff = True
#     #     user.is_superuser = True
#     #     user.save(using=self._db)

#         return user





# class UserManager(BaseUserManager):

#     def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not username:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         GlobalUserModel = apps.get_model(
#             self.model._meta.app_label, self.model._meta.object_name
#         )
#         username = GlobalUserModel.normalize_username(username)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)

#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self._create_user(username, email, password, **extra_fields)
