from django.contrib import admin
from .models import Forum
from .models import Symposium
from .models import Congress, Event

admin.site.register(Forum)
admin.site.register(Symposium)
admin.site.register(Congress)

admin.site.register(Event)