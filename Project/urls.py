from django.conf.urls import include, url
from django.contrib import admin


api_patterns = []

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/books/', include('Books.urls')),
    url(r'^api/v1/users/', include('Accounts.urls')),
    url(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]
