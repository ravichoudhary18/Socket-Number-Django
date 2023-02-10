from django.contrib import admin
from django.urls import path, include
from backend.settings import DEBUG
from .views import home

admin.site.site_title = "Trading"
admin.site.site_header = "Wellcome"
admin.site.index_title = "Hello"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home)
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
