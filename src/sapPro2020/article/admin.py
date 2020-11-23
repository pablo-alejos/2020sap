from django.contrib import admin

from .models import Article
from .models import Journal

admin.site.register(Article)
admin.site.register(Journal)