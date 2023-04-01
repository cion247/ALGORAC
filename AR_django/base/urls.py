from django.urls import path, include

from base.views import LatestNoticelistView

urlpatterns = [
    path('notices/latest/', LatestNoticelistView.as_view()),
]