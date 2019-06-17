# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, User

from django.template import RequestContext
from el_pagination.decorators import page_template
from el_pagination.views import AjaxListView

from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView
        , DetailView
        , CreateView
        , UpdateView
        , DeleteView
        )
from .serializers import PostSerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#****************token****************************
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }

        token = Token.objects.create(user=request.user)
        print(token.key)
        return Response(content)

    def post(self, request, format=None):
        return Response({'received data': request.data})


#****************end token****************************
# from rest_framework import permissions
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user


#****************search filter of rest****************************
from rest_framework import generics

from rest_framework import filters
#from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

#**************** end search filter of rest****************************
@login_required
def like_post(request,):    
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False    
    user = request.user
    # print("#****************end token****************************")    
    # print(post.likes.all())
    # print(post.author.email)
    # print("#****************end token****************************")
    if(user in post.likes.all()):
        print("you DisLiked this post")
        post.likes.remove(request.user)
        is_liked = False
    else:
        print("you Liked this post")
        post.likes.add(request.user)
        is_liked = True
        #+++++++++++++++++++sending mail++++++++++++++++++ 
        import smtplib 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("aleenav1996@gmail.com", "sweetchurch") 
        message = "One person liked your post"
        dest = post.author.email
        s.sendmail("aleenav1996@gmail.com", dest , message) 
        print("success")
        # terminating the session 
        s.quit() 
        #+++++++++++++++++++++++++++++++++++++
    return HttpResponseRedirect(post.get_absolute_url())
# ************************************important**********************************************************
class PostRestView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        # print("*********************")
        # print(self.request.user)
        # print("*********************")
        serializer.save(likes=self.request.User)   
        serializer.save(author=self.request.User) 

# **********************************************************************************************
class PostListView(AjaxListView):
    context_object_name = "posts"
    template_name = "blog/home.html"
    page_template='blog/entry_index.html'
    ordering = ['-date_posted']

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return (super().form_valid(form))
# ///////////////////////////////////////////////////////////////////////////////////////////////////////
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blogs/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
