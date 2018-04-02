# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


# Override default UserManager system to support additional fields and enforce e-mail address as
# the user name.
class AccountUserManager(UserManager):

	"""
	Create and save a User with the given username, e-mail address, and password.
	"""
	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

		now = timezone.now()  # get the current date and time.

		# if no email is supplied, throw an error.
		if not email:
			raise ValueError("A valid e-mail address must be supplied.")

		email = self.normalize_email(email)  # capture the email address

		# create the user
		user = self.model(username=email, email=email, is_staff=is_staff, 
						   is_superuser=is_superuser, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		# return the saved user
		return user

"""
Abstract the User to enable additional fields to be created.
"""
class User(AbstractUser):
	# title field choices
	TITLE_CHOICES = (
		('Mr', 'Mr'),
		('Mrs', 'Mrs'),
		('Miss', "Miss"),
		('Ms', 'Ms'),
		('Dr', 'Dr'),
		('Prof', 'Prof')
	)

	# create the name and billing address fields.
	title = models.CharField(max_length=4, null=True, blank=True, choices=TITLE_CHOICES)  # title field, can be blank.
	first_name = models.CharField(max_length=50, null=False)  # first name field, required.
	last_name = models.CharField(max_length=50, null=False)  # last name field, required.
	telephone = models.CharField(max_length=12, null=True, blank=True)  # telephone number, can be blank.
	post_code = models.CharField(max_length=8, null=False)  # postcode field, required.
	address_line_1 = models.CharField(max_length=100, null=False)  # first line of address, required.
	address_line_2 = models.CharField(max_length=100, null=True, blank=True)  # second line of address (optional).
	address_town = models.CharField(max_length=50, null=True, blank=True)  # town.
	address_city = models.CharField(max_length=50, null=True, blank=True)  # city.
	address_county = models.CharField(max_length=50, null=True, blank=True)  # county.

	# bind fields to AccountUserManager.
	objects = AccountUserManager()
