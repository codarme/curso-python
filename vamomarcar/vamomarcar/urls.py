from django.urls import path
from django.urls.conf import include

from agenda import urls

urlpatterns = [
    path('', include(urls.urlpatterns)),
]
