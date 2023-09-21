# filo_project/filo_project/urls.py


from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# Local imports
from UserApp.views import register, UserLoginView, home_view

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/<uuid:token>/', register, name='register_with_token'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
]

# Serving static files during development
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
