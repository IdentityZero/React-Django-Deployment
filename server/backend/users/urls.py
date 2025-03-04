from django.urls import path

from .views import fetch_users

urlpatterns = [path("", fetch_users)]
