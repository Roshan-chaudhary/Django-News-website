from django.contrib import admin
from django.urls import include,path
from.import views
from .views import *


# For API URL
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'image',ImageViewSet)

# For password Reset 
from django.contrib.auth import views as auth_views

urlpatterns = [
    
  
   path('All/',views.All, name='All'),
   path('home/', views.home, name='home'),
   path('index/', views.index, name='index'),
   path('App/', views.App, name='App'),
   path('New/', views.New, name='New'),
   path('gmail/', views.gmail, name='gmail'),
   path('video/', views.video, name='video'),
   path('a/', views.a, name='a'),
   path('b/', views.b, name='b'),
   
   # Weather 
   path('weather/', views.weather, name='weather'),
   
   
   # Login form 
   path('',views.SignupPage,name='signup'),
   path('fail/',views.fail,name='fail'),
   path('login/',views.LoginPage,name='login'),
   path('logout/',views.LogoutPage,name='logout'),
   
   
   #password Reset
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

   # API URL 
   
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

   # Payment .
    path('khalthi/',views.khalthi,name='khalthi'),
    path('epay/',views.epay,name='epay'),





]