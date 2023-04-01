from django.urls import path, include

from base.views import LatestNoticelistView, NoticedetaleView

urlpatterns = [
    path('notices-latest/', LatestNoticelistView.as_view()),
    path('notices-detals/', NoticedetaleView.as_view()),
]