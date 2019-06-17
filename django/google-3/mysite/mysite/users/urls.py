from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#set namespace
app_name='register'
app_name = 'users'
urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)