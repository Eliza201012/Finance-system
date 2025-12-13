from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.custom_login, name="custom_login")
]
