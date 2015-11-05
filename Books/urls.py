from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'', views.BookViewSet),
    url(r'list', views.ListBooksByGenre.as_view()),
    url(r'genres/', views.ListGenres.as_view())
]

