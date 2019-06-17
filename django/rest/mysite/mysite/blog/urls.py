from django.urls import path, include
from . views import (PostListView
    , PostDetailView
    , PostCreateView
    , PostUpdateView
    ,PostDeleteView
    )
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post',views.PostRestView)#mension path in space given between''
#http://127.0.0.1:8000/blogs/rest_posts/Post/
#set namespace
app_name='blog'

urlpatterns =[
    path('rest_posts/',include(router.urls)),
    path('',PostListView.as_view(), name='blog_home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog_detail'),  
    path('likes', views.like_post, name='like_post'),
    path('new/', PostCreateView.as_view(),name="post_create"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),  
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),  
]

#<app>/<model>_<viewtype>.html