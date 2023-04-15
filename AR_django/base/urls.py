from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from base.views import LatestNoticelistView, MentorView, MyTokenObtainPairView, NoticedetailView, LatestGallerylistView, ProjectView, MessagesView, FeadbackView, UserCreateAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('notices-latest/', LatestNoticelistView.as_view()),
    path('notices-detals/<slug:notice_slug>', NoticedetailView.as_view()),

    path('gallery-latest/', LatestGallerylistView.as_view()),

    path('projects/', ProjectView.as_view()), 

    path('messages/', MessagesView.as_view()),

    path('feadback/', FeadbackView.as_view()),

    path('mentor/', MentorView.as_view()),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/create/', UserCreateAPIView.as_view(), name='user_create')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


