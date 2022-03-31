from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
