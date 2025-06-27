from django.urls import path
from .views import MainView, CreateUser
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", MainView.as_view(), name='main'),
    path("reg/", CreateUser.as_view(), name='reg'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('login/', LoginView.as_view(template_name="registration/login.html"), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)