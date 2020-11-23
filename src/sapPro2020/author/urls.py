from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import AuthorIndexView, AuthorCreateView, AuthorDetailView, AuthorDeleteView, AuthorUpdateView

app_name = 'author'
urlpatterns = [
    path('index', login_required(AuthorIndexView.as_view()), name='author-index'),
    path('create', login_required(AuthorCreateView.as_view()), name='author-create'),
    path('<int:id>/', login_required(AuthorDetailView.as_view()), name='author-detail'),
    path('<int:id>/delete', login_required(AuthorDeleteView.as_view()), name='author-delete'),
    path('<int:id>/update', login_required(AuthorUpdateView.as_view()), name='author-update'),
]