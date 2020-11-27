from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import BookIndexView,BookDetailView,BookCreateView,BookUpdateView,BookDeleteView

app_name = 'book'
urlpatterns = [
    path('',BookIndexView.as_view(),name='book-index'),
    path('create',login_required(BookCreateView.as_view()),name='book-create'), 
    path('<int:id>/',BookDetailView.as_view(),name='book-detail'),  
    path('<int:id>/delete',login_required(BookDeleteView.as_view()),name='book-delete'),
    path('<int:id>/update',login_required(BookUpdateView.as_view()),name='book-update'), 
]