from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Gallery, Notice
from .serializers import GallerySerializer, NoticeSerializer
# Create your views here.

# View for returning the latest 3 notices in the database
class LatestNoticelistView(APIView):
    def get(self, request, format = None):
        # Query the database for the latest 3 notices
        Notices = Notice.objects,all[0:3]
        # Serialize the queryset of notices
        serializer = NoticeSerializer(Notices, many =True)
        # Return serialized data as response
        return Response(serializer.data)