from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import (UserIndexView, UserCreateView,
                    UserDetailView, UserUpdateView, UserChangePasswordView,
                    UserDeleteView, UserSapLoginView, UserSapLogoutView)

app_name = 'userSap'
urlpatterns = [
    path('login', UserSapLoginView.as_view(), name='user-login'),
    path('logout', login_required(UserSapLogoutView), name='user-logout'),
    path('index', login_required(UserIndexView.as_view()), name='user-index'),
    path('create', UserCreateView.as_view(), name='user-create'),
    path('<int:id>/', login_required(UserDetailView.as_view()), name='user-detail'),
    path('<int:id>/delete', login_required(UserDeleteView.as_view()),
         name='user-delete'),
    path('<int:id>/update', login_required(UserUpdateView.as_view()),
         name='user-update'),
    path('<int:id>/changepassword',
         login_required(UserChangePasswordView.as_view()), name='user-update-password'),
]
