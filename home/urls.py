from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home),
    path('resources/', views.resources),
	path('manage/', views.manage),
    path('manage/scoreboard/', views.download_scoreboard),
    path('manage/firstblood/', views.firstblood, name='firstblood'),
    path('manage/users-data/', views.download_user_data),
    path('manage/challenges-data/', views.download_challenges_data),
    path('realtime/', views.solves, name='solves'),
    path('scoreboard-json/', views.scoreboard_json, name='scoreboard-json'),



]