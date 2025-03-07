from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                    PostCreateView)

urlpatterns = [  #trailing slashes will help django redirect blog_route
    path('',PostListView.as_view(), name = 'blog-home'), #home page route 
    path('about/',views.about, name = 'blog-about'),
    path('post/<int:pk>',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post-delete'),
]