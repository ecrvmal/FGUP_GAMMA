from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View, DetailView)
from mainapp.models import Letter, Parcel


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class LetterCreateView(CreateView):
    template_name = "mainapp/letter_form.html"
    model = Letter
    fields = ['sender_name',
              'sender_surname',
              'from_address',
              'to_address',
              'from_index',
              'to_index',
              'letter_type',
              'letter_weight',
              ]

    def get_success_url(self):
        return reverse('letters_list')


class LetterListView(ListView):
    model = Letter
    template_name = "letter_list.html"

    def get_queryset(self):
        return Letter.objects.all()


class LetterUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Letter
    fields = ['sender_name',
              'sender_surname',
              'from_address',
              'to_address',
              'from_index',
              'to_index',
              'letter_type',
              'letter_weight',
              ]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("letter_view", kwargs={"pk": pk})


class LetterView(DetailView):
    model = Letter


class LetterDeleteView(DeleteView):
    model = Letter
    template_name = "mainapp/letter_confirm_delete.html"

    def get_success_url(self):
        return reverse('letters_list')


class ParcelCreateView(CreateView):
    template_name = "mainapp/parcel_form.html"
    model = Parcel
    fields = ['sender_name',
              'sender_surname',
              'from_address',
              'to_address',
              'from_index',
              'to_index',
              'phone',
              'parcel_type',
              'price',
              ]

    def get_success_url(self):
        return reverse('parcels_list')


class ParcelListView(ListView):
    model = Parcel
    template_name = "parcel_list.html"

    def get_queryset(self):
        return Parcel.objects.all()


class ParcelUpdateView(UpdateView):
    template_name_suffix = "_update_form"
    model = Parcel
    fields = ['sender_name',
              'sender_surname',
              'from_address',
              'to_address',
              'from_index',
              'to_index',
              'phone',
              'parcel_type',
              'price',
              ]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("parcel_view", kwargs={"pk": pk})


class ParcelView(DetailView):
    model = Parcel


class ParcelDeleteView(DeleteView):
    model = Parcel
    template_name = "mainapp/parcel_confirm_delete.html"

    def get_success_url(self):
        return reverse('parcels_list')


