
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.users.urls')),
    url(r'^travels/', include('apps.trips.urls')),
]
