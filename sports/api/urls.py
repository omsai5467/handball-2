
from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path("songs/<id>",views.playsongs),
  path("freedom/<id>",views.freedom),
  path("greet",views.greet),
  path("home",views.home),
  path("blogs",views.blogposts),
  path("getPlayers",views.getPlayers),
  path("news",views.news),
  path("matches",views.match),
  path("getp/<playerId>/",views.getP),
  path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path("getBlog/<id>/",views.getBlog)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)