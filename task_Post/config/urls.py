
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    # path("mainapp/", RedirectView.as_view(url="mainapp/")),
    path("", include("mainapp.urls")),
]
