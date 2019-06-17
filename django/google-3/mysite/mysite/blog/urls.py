from django.urls import path
from . views import (PostListView
    , PostDetailView
    , PostCreateView
    , PostUpdateView
    ,PostDeleteView
    )
from .import views

#set namespace
app_name='blog'

urlpatterns =[
    path('',PostListView.as_view(), name='blog_home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog_detail'),  
    path('likes', views.like_post, name='like_post'),
    path('new/', PostCreateView.as_view(),name="post_create"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),  
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),  
]

#<app>/<model>_<viewtype>.html