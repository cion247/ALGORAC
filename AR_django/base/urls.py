from django.urls import path, include

from base.views import LatestNoticelistView, NoticedetaleView, LatestGallerylistView

urlpatterns = [
    path('notices-latest/', LatestNoticelistView.as_view()),
    path('notices-detals/<slug:notice_slug>', NoticedetaleView.as_view()),
    path('gallery-latest/', LatestGallerylistView.as_view()),
]
