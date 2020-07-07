from django.urls import path
from . import views
# Add URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('user-home/', views.user_home, name='user-home'),
    path('play/', views.play, name='play'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
