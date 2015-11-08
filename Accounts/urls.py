from rest_framework import routers
from . import views


urlpatterns = []

video_router = routers.SimpleRouter()
video_router.register(r'books', views.BookViewSet, base_name='books_view_set')
urlpatterns += video_router.urls
