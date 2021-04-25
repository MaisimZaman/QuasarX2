from django.urls import path
from video.views import video_view, VideoCreateView, VideoDetailView, VideoView

urlpatterns = [
    path('videos/', VideoView.as_view(), name='videos-home'),
    path('videos/post', VideoCreateView, name='video-create'),
    path('videos/<int:pk>/', VideoDetailView, name='video-detail')
]
