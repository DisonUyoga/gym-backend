from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", views.user_create_view, name="user-view" ),
    path("token/", TokenObtainPairView.as_view(), name="token-view")
]
