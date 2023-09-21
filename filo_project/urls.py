# filo_project/filo_project/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from UserApp.views import register, UserLoginView
from UserApp.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/<uuid:token>/', register, name='register_with_token'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
]

