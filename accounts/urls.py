from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", views.logout_profile, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.custom_login, name="custom_login"),
    path("balance/add_money/", views.add_money_to_balance, name="add_money_to_balance")
]
