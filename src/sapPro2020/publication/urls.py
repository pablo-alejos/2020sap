from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from .views import PublicationView,SearchView,searchAjaxView,objectAjaxView

app_name = 'publication'
urlpatterns = [
    path('', PublicationView.as_view(), name='publication-index'),
    path('buscar/', SearchView.as_view(), name='publication-filter'),
    path('response/', searchAjaxView,name="response"),
    path('producto/', objectAjaxView,name="objectResponse"),
]
