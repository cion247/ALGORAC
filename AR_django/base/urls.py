from django.urls import path, include

from base.views import LatestNoticelistView, MentorView, NoticedetailView, LatestGallerylistView, ProjectView, MessagesView, SignupAPIView, LoginAPIView, FeadbackView, RegisterUser
from usermodel.views import APILogoutView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
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

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout_token/', APILogoutView.as_view(), name='logout_token'),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/',RegisterUser.as_view())
]


