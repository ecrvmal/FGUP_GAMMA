from django.urls import path
from mainapp import views


urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("index", views.MainPageView.as_view()),
    path("letter_create/", views.LetterCreateView.as_view(), name="letter_create"),
    path("letter_list/", views.LetterListView.as_view(), name="letters_list"),
    path("letter_update/<int:pk>/", views.LetterUpdateView.as_view(), name="letter_update"),
    path("letter_view/<int:pk>/", views.LetterView.as_view(), name="letter_view",),
    path("letter_delete/<int:pk>/", views.LetterDeleteView.as_view(), name="letter_delete", ),
    path("parcel_create/", views.ParcelCreateView.as_view(), name="parcel_create"),
    path("parcel_list/", views.ParcelListView.as_view(), name="parcels_list"),
    path("parcel_update/<int:pk>/", views.ParcelUpdateView.as_view(), name="parcel_update"),
    path("parcel_view/<int:pk>/", views.ParcelView.as_view(), name="parcel_view", ),
    path("parcel_delete/<int:pk>/", views.ParcelDeleteView.as_view(), name="parcel_delete", ),
]
