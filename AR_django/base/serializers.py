
from rest_framework import serializers

from .models import Gallery, Notice
from django.contrib.auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class ProgectSerializer(serializers.ModelSerializer):
    pass


class MassagesSerializer(serializers.ModelSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    pass
