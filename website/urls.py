from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("about/", about_view),
    path("index/", index_view)
]
