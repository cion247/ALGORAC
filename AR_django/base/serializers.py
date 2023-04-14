
from httplib2 import Authentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

from .models import Gallery, Mentor, Notice, projects, messages, Feadback
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


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


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    tokens = serializers.SerializerMethodField()  # New field to hold tokens

    def get_tokens(self, obj):  # Method to generate tokens
        user = obj['user']
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = Authentication(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'No user found with this username.'
            )

        return {
            "user": user,
            "username": user.username,
            "email": user.email,
            "tokens": self.get_tokens({"user": user}),
        }