from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from article import views
from account import views
from book import views
from bookChapter import views
from userSap import views
from project import views
from publication import views
from author import views
from .views import HomeView,SearchView,searchAjaxView,tagsAjaxView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name = "home"),
    path('busqueda/', SearchView.as_view(),name="search"),
    #path('response/', searchAjaxView,name="response"),
    path('tags/', tagsAjaxView,name="tags"),    
    path('publicaciones/', include('publication.urls')),
    path('usuario/', include('userSap.urls')),
    path('cuenta/', include('account.urls')),
    path('articulo/', include('article.urls')),
    path('libro/', include('book.urls')),
    path('capitulo/', include('bookChapter.urls')),
    path('etiqueta/', include('tag.urls')),
    path('proyecto/', include('project.urls')),
    path('evento/', include('event.urls')),
    path('autores/', include('author.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
