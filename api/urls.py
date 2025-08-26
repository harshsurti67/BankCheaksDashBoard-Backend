from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='user-signup'),
     path("user/profile/", views.user_profile, name="user-profile"),
    path('login/', views.login, name='user-login'),
]
