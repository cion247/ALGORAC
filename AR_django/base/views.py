from django.http import Http404
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gallery, Mentor, Notice, projects
from .serializers import GallerySerializer, MentorSerializer, NoticeSerializer, ProjectSerializer, MessagesSerializer, FeadbackSerializer
# Create your views here.

from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class SignupAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(res)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(res)


class LatestNoticelistView(APIView):
    def get(self, request, format=None):
        notices = list(Notice.objects.all()[0:7])
        if not notices:
            return Response({'message': 'No data found'})
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)


class NoticedetailView(APIView):
    def get_object(self, notice_slug):
        try:
            return Notice.objects.get(slug=notice_slug)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, notice_slug, format=None):
        Notices = self.get_object(notice_slug)
        serializer = NoticeSerializer(Notices)
        return Response(serializer.data)


class LatestGallerylistView(APIView):
    def get(self, request, format=None):
        Gallerys = Gallery.objects.all()[:6]
        if not Gallerys:
            return Response({'message': 'No data found'})
        serializer = GallerySerializer(Gallerys, many=True)
        return Response(serializer.data)


class FullGalleryView(APIView):
    def get_object(self, notice_slug):
        try:
            return Notice.objects.get(slug=notice_slug)
        except Notice.DoesNotExist:
            raise Http404

    def get(self, notice_slug, format=None):
        Notices = self.get_object(notice_slug)
        serializer = NoticeSerializer(Notices)
        return Response(serializer.data)


class ProjectView(APIView):
    def get(self, request, format=None):
        project = projects.objects.all()
        if not project:
            # Corrected variable name
            return Response({'message': 'No data found'})
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class MessagesView(APIView):
    def post(self, request, format=None):
        massages = MessagesSerializer(data=request.data)
        if massages.is_valid():
            massages.save()
            return Response(massages.data, status=status.HTTP_201_CREATED)
        return Response(massages.errors, status=status.HTTP_400_BAD_REQUEST)


class FeadbackView(APIView):
    def post(self, request, format=None):
        massages = FeadbackSerializer(data=request.data)
        if massages.is_valid():
            massages.save()
            return Response(massages.data, status=status.HTTP_201_CREATED)
        return Response(massages.errors, status=status.HTTP_400_BAD_REQUEST)


class MentorView(APIView):
    def post(self, request, format=None):
        mentor = Mentor.objects.all()
        if not mentor:
            return Response({'message': 'No data found'})
        serializer = MentorSerializer(mentor, many=True)
        return Response(serializer.data)


class RegisterUser(APIView):
    def post(self, request):
        serializer= UserSerializer(data= request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'fsfdsfsd'})
        
        serializer.save()

        user= User.objects.get(username=serializer.data['username'])
        token_obj , _=   Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj)})
