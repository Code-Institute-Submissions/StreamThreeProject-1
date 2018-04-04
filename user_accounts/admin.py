# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User

# Admin configuration for User Accounts.
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'date_joined', 'is_staff')


# add User Accounts to admin screen.
admin.site.register(User, UserAdmin)