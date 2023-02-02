from .models import *
from rest_framework import serializers


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = appmodel
        fields = '__all__'
