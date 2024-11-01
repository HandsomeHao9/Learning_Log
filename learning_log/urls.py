from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles import views
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
    re_path(r'^static/(?P<path>.*)$', views.serve),
]
