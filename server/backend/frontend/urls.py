from django.urls import re_path

from .views import main

urlpatterns = [
    re_path(r"^(?P<path>.*)$", main),
]
