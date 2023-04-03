
from rest_framework import serializers

from .models import Gallery, Notice, projects, messages
from django.contrib.auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    pass
