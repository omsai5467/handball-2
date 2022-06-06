"""sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

  path("home",views.home),
  path("blogs",views.blogposts),
  path("getPlayers",views.getPlayers),
  path("news",views.news),
  path("matches",views.match),
  path("getp/<playerId>/",views.getP)
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)