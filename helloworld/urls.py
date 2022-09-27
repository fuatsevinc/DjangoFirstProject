from urllib.request import Request
from django.urls import path


urlpatterns = [
    path("", Request(hellword.urls)),
]