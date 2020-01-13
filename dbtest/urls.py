"""dbtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from db import views
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from db.views import current_user, UserList 


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/current_user/$', current_user),
    re_path('^api/register/$', UserList.as_view()),
    re_path('^api/departments/$', views.departments),
    re_path('^api/competency-results/$', views.competency_results),
    re_path('^api/moringa-staff/$', views.moringa_staff),
    re_path('^api/token_auth/$',obtain_jwt_token),
    re_path('^api/signin/$', views.handle_login),
]
