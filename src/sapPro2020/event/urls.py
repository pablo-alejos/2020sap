from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (ForumIndexView, ForumCreateView, ForumDetailView, ForumUpdateView, ForumDeleteView)
from .views import (SymposiumIndexView, SymposiumCreateView, SymposiumDetailView, SymposiumUpdateView, SymposiumDeleteView)
from .views import (CongressIndexView, CongressCreateView, CongressDetailView, CongressUpdateView, CongressDeleteView)
from .views import (EventIndexView)
app_name = 'event'
urlpatterns = [
    path('index',
          EventIndexView.as_view(),name='event-index'),
    path('foro/index',
         login_required(ForumIndexView.as_view()), name='forum-index'),
    path('foro/create',
         login_required(ForumCreateView.as_view()), name='forum-create'),
    path('foro/<int:id>/',
         login_required(ForumDetailView.as_view()), name='forum-detail'),
    path('foro/<int:id>/delete',
         login_required(ForumDeleteView.as_view()), name='forum-delete'),
    path('foro/<int:id>/update',
         ForumUpdateView.as_view(), name='forum-update'),

    path('simposio/index',
         login_required(SymposiumIndexView.as_view()), name='symposium-index'),
    path('simposio/create',
         login_required(SymposiumCreateView.as_view()), name='symposium-create'),
    path('simposio/<int:id>/',
         login_required(SymposiumDetailView.as_view()), name='symposium-detail'),
    path('simposio/<int:id>/delete',
         login_required(SymposiumDeleteView.as_view()), name='symposium-delete'),
    path('simposio/<int:id>/update',
         login_required(SymposiumUpdateView.as_view()), name='symposium-update'),

    path('congreso/index',
         login_required(CongressIndexView.as_view()), name='congress-index'),
    path('congreso/create',
         login_required(CongressCreateView.as_view()), name='congress-create'),
    path('congreso/<int:id>/',
         login_required(CongressDetailView.as_view()), name='congress-detail'),
    path('congreso/<int:id>/delete',
         login_required(CongressDeleteView.as_view()), name='congress-delete'),
    path('congreso/<int:id>/update',
         login_required(CongressUpdateView.as_view()), name='congress-update'),

    
]