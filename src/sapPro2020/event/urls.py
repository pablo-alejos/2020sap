from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (EventIndexView, EventCreateView, EventUpdateView, EventDeleteView)
app_name = 'event'
urlpatterns = [

    path('index/',
         login_required(EventIndexView.as_view()), name='event-index'),
    path('create/',
         login_required(EventCreateView.as_view()), name='event-create'),
    path('update/<int:id>/',
         login_required(EventUpdateView.as_view()), name='event-update'),
     path('delete/<int:id>/',
         login_required(EventDeleteView.as_view()), name='event-delete'),

]
