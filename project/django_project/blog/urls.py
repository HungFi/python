from django.urls import path
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/filter/', views.blog_filter, name='post-filter'),
    path('post/count/', views.blog_count, name='post-count')
]
