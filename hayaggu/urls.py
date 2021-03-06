"""hayaggu URL Configuration

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

from server import api

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^demo/list$', api.demo_list),
    url(r'^demo/(?P<demo_id>\d+)$', api.demo_detail),

    url(r'^comment/list$', api.comment_list),
    url(r'^comment/new$', api.add_comment),

    url(r'^blinker/list$', api.get_blinkers),
    url(r'^blinker/new$', api.add_blinker),
]
