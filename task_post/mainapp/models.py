from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config import settings
from config.settings import PARCEL_TYPES, LETTER_TYPES


def get_letter_types():
    return {i: i for i in settings.LETTER_TYPES}


def get_parcel_types():
    return {i: i for i in settings.PARCEL_TYPES}


class PostItem(models.Model):
    sender_name = models.CharField(max_length=128, blank=False)
    sender_surname = models.CharField(max_length=128, blank=False)
    from_address = models.CharField(max_length=128, blank=False)
    to_address = models.CharField(max_length=128, blank=False)
    from_index = models.PositiveIntegerField(blank=False)
    to_index = models.PositiveIntegerField(blank=False)

    class Meta:
        abstract = True


class Letter(PostItem):
    letter_type = models.IntegerField(choices=LETTER_TYPES, default=1)
    letter_weight = models.PositiveIntegerField(default=0)

    objects = models.Manager()


class Parcel(PostItem):
    phone = PhoneNumberField(blank=True)
    parcel_type = models.IntegerField(choices=PARCEL_TYPES, default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()



