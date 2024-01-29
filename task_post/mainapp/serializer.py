from rest_framework.serializers import ModelSerializer

from mainapp.models import Letter, Parcel

# This module returns object (serialized data)


class LetterModelSerializer(ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'


class ParcelModelSerializer(ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
