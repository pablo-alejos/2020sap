from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import ProjectIndexView,ProjectDetailView,ProjectCreateView,ProjectUpdateView,ProjectDeleteView

app_name = 'project'
urlpatterns = [
    path('index',login_required(ProjectIndexView.as_view()),name='project-index'),
    path('create',login_required(ProjectDetailView.as_view()),name='project-create'), 
    path('<int:id>/',(ProjectCreateView.as_view()),name='project-detail'),  
    path('<int:id>/delete',(ProjectUpdateView.as_view()),name='project-delete'),
    path('<int:id>/update',(ProjectDeleteView.as_view()),name='project-update'), 
]