from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import (UserIndexView, UserCreateView,
                    UserDetailView, UserUpdateView, UserChangePasswordView,
                    UserDeleteView, UserSapLoginView, UserSapLogoutView,PublicationUserView)

from .views import AcademyIndexView, AcademyCreateView, AcademyDetailView, AcademyUpdateView, AcademyDeleteView
from .views import ProgramIndexView, ProgramCreateView, ProgramDetailView, ProgramUpdateView, ProgramDeleteView
from .views import AccountIndexView, AccountCompleteView, AccountDetailView, AccountUpdateView, AccountDeleteView


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
    path('mis_productos', PublicationUserView.as_view(), name='user-product-panel'),


    path('cuerpo_academico/index',
         login_required(AcademyIndexView.as_view()), name='academy-index'),
    path('cuerpo_academico/create',
         login_required(AcademyCreateView.as_view()), name='academy-create'),
    path('cuerpo_academico/<int:id>/',
         login_required(AcademyDetailView.as_view()), name='academy-detail'),
    path('cuerpo_academico/<int:id>/delete',
         login_required(AcademyDeleteView.as_view()), name='academy-delete'),
    path('cuerpo_academico/<int:id>/update',
         AcademyUpdateView.as_view(), name='academy-update'),

    path('programa_educativo/index',
         login_required(ProgramIndexView.as_view()), name='program-index'),
    path('programa_educativo/create',
         login_required(ProgramCreateView.as_view()), name='program-create'),
    path('programa_educativo/<int:id>/',
         login_required(ProgramDetailView.as_view()), name='program-detail'),
    path('programa_educativo/<int:id>/delete',
         login_required(ProgramDeleteView.as_view()), name='program-delete'),
    path('programa_educativo/<int:id>/update',
         login_required(ProgramUpdateView.as_view()), name='program-update'),

    path('index', login_required(AccountIndexView.as_view()), name='account-index'),
    #path('create', login_required(AccountCreateView.as_view()), name='account-create'),
    path('cuenta/<int:id>/complete', login_required(AccountCompleteView.as_view()), name='account-complete'),
    path('cuenta/<int:id>/', login_required(AccountDetailView.as_view()), name='account-detail'),
    path('cuenta/<int:id>/delete', login_required(AccountDeleteView.as_view()), name='account-delete'),
    path('cuenta/<int:id>/update', login_required(AccountUpdateView.as_view()), name='account-update'),
]
