from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'main/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wort', views.wort , name="wort"),
    path('create', views.create, name="create"),
    path('post', views.add_wort)

]