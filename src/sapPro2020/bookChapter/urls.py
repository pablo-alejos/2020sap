from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import BookChapterIndexView,BookChapterDetailView,BookChapterCreateView,BookChapterUpdateView,BookChapterDeleteView

app_name = 'bookChapter'
urlpatterns = [
    path('index',BookChapterIndexView.as_view(),name='bookChapter-index'),
    path('create',login_required(BookChapterCreateView.as_view()),name='bookChapter-create'), 
    path('<int:id>/',login_required(BookChapterDetailView.as_view()),name='bookChapter-detail'),  
    path('<int:id>/delete',login_required(BookChapterDeleteView.as_view()),name='bookChapter-delete'),
    path('<int:id>/update',login_required(BookChapterUpdateView.as_view()),name='bookChapter-update'), 
]