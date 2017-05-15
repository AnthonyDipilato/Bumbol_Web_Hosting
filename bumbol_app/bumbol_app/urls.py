"""bumbol_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.build_page, {'page':'home'}),
    url(r'^about$', views.build_page, {'page':'about'}),
    url(r'^services$', views.build_page, {'page':'services'}),
    url(r'^contact$', views.build_page, {'page':'contact'}),
    url(r'^projects$', views.build_projects_page, {'page':'projects'}),
    url(r'^projects/(?P<gallery_id>[0-9]+)$', views.build_gallery_page),
    url(r'^projects/(?P<slug>[\w-]+)$', views.build_category_page),
    url(r'^bids/(?P<page>[\w]{1,12})$', views.build_bid_page),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
