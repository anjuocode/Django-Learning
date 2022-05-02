from dataclasses import fields
from re import T
from django.forms import models
from rest_framework import serializers
from.models import Try

class try_ser(serializers.ModelSerializer):
    class Meta:
        model=Try
        fields="__all__"