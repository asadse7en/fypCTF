from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home),
	path('manage/', views.manage),
    path('manage/scoreboard/', views.download_scoreboard),
    path('manage/users-data/', views.download_user_data)

]