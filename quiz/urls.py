from django.urls import path
from . import views
# Add URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play, name='play'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('user-home/', views.user_home, name='user-home'),
    path('submission-result/<int:attempted_question_pk>/', views.submission_result, name='submission_result'),
    
]
