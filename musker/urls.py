from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('profile_list/',views.profile_list,name='profile_list'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('user_login',views.user_login,name='login'),
    path('user_logout',views.user_logout,name='logout'),
    path('signin',views.signin,name='signin'),
    path('update_user',views.update_user,name='update_user'),
    path('meep_like\<int:pk>',views.meep_like,name='meep_like'),
    path('meep_show\<int:pk>',views.meep_show,name='meep_show'),
    path('unfollow/<int:pk>',views.unfollow,name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
]
