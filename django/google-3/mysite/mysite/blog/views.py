# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

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

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
@login_required
def like_post(request,):    
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False    
    user = request.user.id
    if(Post.likes.user == user):
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
# def like_post(request,): 
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))   
#     post.likes.add(request.user)
#     return HttpResponseRedirect(post.get_absolute_url())
   
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     #paginate_by = 2




# @page_template('entry_index_page.html')

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
