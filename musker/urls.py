from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('profile_list/',views.profile_list,name='profile_list'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('user_login',views.user_login,name='login'),
    path('user_logout',views.user_logout,name='logout'),
]