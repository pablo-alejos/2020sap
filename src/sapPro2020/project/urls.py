from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import ProjectIndexView,ProjectDetailView,ProjectCreateView,ProjectUpdateView,ProjectDeleteView,ProjectJoinView

app_name = 'project'
urlpatterns = [
    path('index',login_required(ProjectIndexView.as_view()),name='project-index'),
    path('create',login_required(ProjectCreateView.as_view()),name='project-create'), 
    path('<int:id>/',(ProjectDetailView.as_view()),name='project-detail'),  
    path('<int:id>/delete',(ProjectDeleteView.as_view()),name='project-delete'),
    path('<int:id>/update',(ProjectUpdateView.as_view()),name='project-update'), 
    path('join',(ProjectJoinView.as_view()),name='project-join'), 
]