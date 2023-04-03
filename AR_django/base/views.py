from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Gallery, Notice, projects
from .serializers import GallerySerializer, NoticeSerializer, ProjectSerializer, MessagesSerializer
# Create your views here.


class LatestNoticelistView(APIView):
    def get(self, request, format=None):
        notices = Notice.objects.all()[:3]
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
        Gallerys = Gallery.objects.all()[:3]
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
        project = projects.objects.all()  # Corrected variable name
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
        
    
    def post(self, request, format=None):
        project = projects.objects.all()  # Corrected variable name
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
     
class MessagesView(APIView):
     def get(self, request, format=None):
        message = message.objects.all()
        serializer = MessagesSerializer(message, many=True)
        return Response(serializer.data)


class RegisterUserView(APIView):
    pass


class LoginUserView(APIView):
    pass


class LogoutUserView(APIView):
    pass


class FullGalleryView(APIView):
    pass