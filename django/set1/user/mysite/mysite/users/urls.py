from django.urls import path
from . import views

#set namespace
app_name='register'
urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),

]