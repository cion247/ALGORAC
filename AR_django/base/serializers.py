from rest_framework import serializers

from .models import Gallery, Mentor, Notice, projects, messages, Feadback

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            "id",
            "topic",
            "Slug",
            "description",
            "date_added"
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'


class FeadbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feadback
        fields = '__all__'
