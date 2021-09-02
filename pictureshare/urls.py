from django.conf.urls import url, include
from django.contrib import admin

# URLS
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('pictures.urls')),
]
