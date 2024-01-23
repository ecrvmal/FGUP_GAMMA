from django.db import models

from task_Post.config import settings


def get_letter_types():
    return {i: i for i in settings.LETTER_TYPES}


def get_parcel_types():
    return {i: i for i in settings.PARCEL_TYPES}


class PostItem(models.Model):
    sender_name = models.CharField(max_length=128, blank=False)
    sender_surname = models.CharField(max_length=128, blank=False)
    from_address = models.CharField(max_length=128, blank=False)
    to_address = models.CharField(max_length=128, blank=False)
    from_index = models.CharField(max_length=128, blank=False)
    to_index = models.CharField(max_length=128, blank=False)

    class Meta:
        abstract = True


class LetterType(models.Model):
    letter_type = models.CharField(max_length=3, choices=get_parcel_types)


class Letter(PostItem):
    letter_type = models.ForeignKey(LetterType, on_delete=models.CASCADE, related_name="letter_type")
    letter_weight = models.PositiveIntegerField(default=0)


class ParcelType(models.Model):
    parcel_type = models.CharField(max_length=3, choices=get_parcel_types)


class Parcel(PostItem):
    phone = models.CharField(max_length=128, blank=True)
    parcel_type = models.ForeignKey(ParcelType, on_delete=models.CASCADE, related_name="letter_type")
    price = models.DecimalField(max_digits=6, decimal_places=2)



