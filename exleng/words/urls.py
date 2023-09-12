from django.urls import path

from .views import *

urlpatterns = [
     path('words/', index, name='words'),
     path('', welcome, name='home'),
     path('test/', test, name='test'),
     path('register/', RegisterUser.as_view(),name='register'),
     path('login/', LoginUser.as_view(), name='login'),
     path('logout/', logout_user, name='logout'),
 ]