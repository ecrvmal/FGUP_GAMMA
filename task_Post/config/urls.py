"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", RedirectView.as_view(url="mainapp/")),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.MainPageView.as_view(), name="index"),
    path("letter_create/", views.LetterCreateView.as_view(), name="letter_create"),
    path("letter_list/", views.LetterListView.as_view(), name="letters_list"),
    path("letter_update/<int:pk>/", views.LetterUpdateView.as_view(), name="letter_update"),
    path("letter_view/<int:pk>/", views.LetterView.as_view(), name="letter_view",),
    path("letter_delete/<int:pk>/", views.LetterDeleeteView.as_view(), name="letter_delete", ),
    path("parcel_create/", views.ParcelCreateView.as_view(), name="parcel_create"),
    path("parcel_list/", views.ParcelListView.as_view(), name="parcels_list"),
    path("parcel_update/<int:pk>/", views.ParcelUpdateView.as_view(), name="parcel_update"),
    path("parcel_view/<int:pk>/", views.ParcelView.as_view(), name="parcel_view", ),
    path("parcel_delete/<int:pk>/", views.ParcelDeleteView.as_view(), name="parcel_delete", ),
]
