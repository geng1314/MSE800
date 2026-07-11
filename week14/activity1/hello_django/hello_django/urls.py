from django.http import HttpRequest, HttpResponse
from django.contrib import admin
from django.urls import path

def hello(request: HttpRequest):
    """Display the Hello Django page."""
    return HttpResponse("<h1>Hello Django , Hello World</h1>")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hello),
]