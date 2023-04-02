from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Gallery, Notice
from .serializers import GallerySerializer, NoticeSerializer
# Create your views here.


class LatestNoticelistView(APIView):
    def get(self, request, format=None):
        Notices = Notice.objects.all()[0:3]
        serializer = NoticeSerializer(Notices, many=True)
        return Response(serializer.data)


class NoticedetaleView(APIView):
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
        Gallerys = Gallery.objects.all()[0:3]
        serializer = GallerySerializer(Gallerys, many=True)
        return Response(serializer.data)


class FullGalleryView(APIView):
    pass


class ProgectView(APIView):
    pass


class MassgesView(APIView):
    pass

class RegisterUserView(APIView):
    pass


class LoginUserView(APIView):
    pass


class LogoutUserView(APIView):
    pass
