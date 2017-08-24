"""dao_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.index_login),
    url(r'^logout/$', views.acc_logout,name='logout'),
    url(r'^dashboard/$', views.dashboard,name='dashboard'),
    url(r'^dashboard/logs/$', views.logs, name='logs'),
    url(r'^download_log/$', views.download_log, name='download_log') ,
    url(r'^update_log/$', views.update_log, name='update_log'),
    url(r'^dir_log/$', views.dir_log, name='dir_log'),
]
