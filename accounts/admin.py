from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Account

admin.site.register(Account)
admin.site.register(User)
