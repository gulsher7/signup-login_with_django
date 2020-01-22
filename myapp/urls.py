from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('userdata/', views.userdata, name='userdata'),
    path('logout/', views.logout, name='logout'),
    
]
