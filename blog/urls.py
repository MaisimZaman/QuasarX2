from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, topics, TopicView, topic_search_view, like_posts, liked_posts
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    #path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView, name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('topics/', topics, name='topics-list'),
    path('topic/<str:name>/', TopicView, name='topic-view'),
    path('topics/search/', topic_search_view, name="search-topics"),
    path('like/', like_posts, name='like-post-view'),
    path('liked_posts/', liked_posts, name='liked-posts')
]




