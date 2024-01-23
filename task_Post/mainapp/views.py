from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)


class LetterCreateView(CreateView):
    template_name = "LetterCreate.html"


class LetterListView(ListView):
    template_name = "LetterCreate.html"


class LetterUpdateView(UpdateView):
    template_name = "letter_update.html"


class LetterView(View):
    template_name = "letter.html"


class LetterDeleteView(DeleteView):
    template_name = "letter_delete.html"


class ParcelCreateView(CreateView):
    template_name = "parcel_create.html"


class ParcelListView(ListView):
    template_name = "parcel_list.html"


class ParcelUpdateView(UpdateView):
    template_name = "parcel_list.html"


class ParcelView(View):
    template_name = "parcel.html"


class ParcelDeleteView(DeleteView):
    template_name = "parcel_delete.html"