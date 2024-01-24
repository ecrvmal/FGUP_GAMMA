from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse

from mainapp import models as mainapp_models


class TestMainPage(TestCase):
    fixtures = ("fixtures/001_all.json",)

    def test_page_open(self):
        path = reverse("index")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)


class TestLetterPages(TestCase):
    fixtures = ("fixtures/001_all.json",)

    def test_page_open_letter_list(self):
        path = reverse("letters_list")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_get_letter_object(self):
        letter_obj = mainapp_models.Letter.objects.first()
        path = reverse("letter_view", args=[letter_obj.pk])
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)


class TestParcelPages(TestCase):
    fixtures = ("fixtures/001_all.json",)

    def test_page_open_parcel_list(self):
        path = reverse("parcels_list")
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_page_open_parcel_detail(self):
        parcel_obj = mainapp_models.Parcel.objects.first()
        path = reverse("parcel_view", args=[parcel_obj.pk])
        result = self.client.get(path)
        self.assertEqual(result.status_code, HTTPStatus.OK)


