from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import ArticleIndexView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView
from .views import JournalIndexView,JournalDetailView,JournalCreateView,JournalUpdateView,JournalDeleteView
app_name = 'article'
urlpatterns = [
    path('',ArticleIndexView.as_view(),name='article-index'),
    path('create',login_required(ArticleCreateView.as_view()),name='article-create'), 
    path('<int:id>/',login_required(ArticleDetailView.as_view()),name='article-detail'),  
    path('<int:id>/delete',login_required(ArticleDeleteView.as_view()),name='article-delete'),
    path('<int:id>/update',login_required(ArticleUpdateView.as_view()),name='article-update'), 

    path('',JournalIndexView.as_view(),name='journal-index'),
    path('create',login_required(JournalCreateView.as_view()),name='journal-create'), 
    path('<int:id>/',login_required(JournalDetailView.as_view()),name='journal-detail'),  
    path('<int:id>/delete',login_required(JournalDeleteView.as_view()),name='journal-delete'),
    path('<int:id>/update',login_required(JournalUpdateView.as_view()),name='journal-update'), 

]