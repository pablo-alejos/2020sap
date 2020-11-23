from django.contrib import admin

from .models import Account
from .models import Academy
from .models import Program

admin.site.register(Account)
admin.site.register(Academy)
admin.site.register(Program)