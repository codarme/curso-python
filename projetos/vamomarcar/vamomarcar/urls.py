from django.urls import path
from django.urls.conf import include
from django.contrib import admin

from agenda import urls

urlpatterns = [
    path('', include(urls.urlpatterns)),
    path('admin/', admin.site.urls),
]
