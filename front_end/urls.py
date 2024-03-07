from django.urls import path
from app.views import home, watermark
from app.views.auth import login, register, logout

urlpatterns = [
    path('',home.HomeView,name='home'),
    path('watermark/',watermark.WatermarkView,name='watermark'),
    path('login/',login.LoginView,name='login'),
    path('register/',register.RegisterView,name='register'),
    path('logout/',logout.LogoutView,name='logout'),
]
