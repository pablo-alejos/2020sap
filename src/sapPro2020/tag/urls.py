from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (TagIndexView, TagCreateView, TagUpdateView, TagDeleteView)

app_name = 'tag'
urlpatterns = [
    path('index', login_required(TagIndexView.as_view()), name='tag-index'),
    path('create', login_required(TagCreateView.as_view()), name='tag-create'),
    path('<int:id>/update',login_required(TagUpdateView.as_view()), name='tag-update'),
    path('<int:id>/delete',login_required(TagDeleteView.as_view()), name='tag-delete'),
]