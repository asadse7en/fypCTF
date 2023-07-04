from django.urls import path, include, re_path
from . import views as manual_views
from . import forms
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', manual_views.redirect, name="redirect"),
	path('login/', auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=forms.LoginForm), name='login'),
	path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	path('register/', manual_views.register, name="register"),
	path('profile/', manual_views.profile, name="profile"),
	path('user/', manual_views.team_view, name="team_view"),
	re_path('user/(?P<pk>.+)', manual_views.every_team, name="every_team"),
	path('profile/changepassword/', manual_views.update_password, name="update_password"),
    path('profile/update-affiliation/', manual_views.update_affiliation, name='update_affiliation'),

]
