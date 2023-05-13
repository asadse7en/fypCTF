from django.shortcuts import render, redirect
from fypCTF.config import name, start_time, end_time

# Create your views here.

def home(request) :
	return render(request, 'home.html', {'name': name(), 'start_time':start_time(), 'end_time':end_time()})

def manage(request) :
		if request.user.is_superuser :
			return render(request, 'manage.html', {'name': name()})
		else :
			return redirect("/")



import csv
from django.http import HttpResponse
from accounts.models import Teams

def download_scoreboard(request):
    scoreboard_data = Teams.objects.order_by("-points")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'
    writer = csv.writer(response)
    writer.writerow(['#', 'Team Name', 'Points'])
    for rank, entry in enumerate(scoreboard_data, start=1):
        writer.writerow([rank, entry.teamname, entry.points])

    return response

def download_user_data(request):
    user_data = Teams.objects.all().order_by('teamname')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['#', 'First Name', 'Last Name', 'Username', 'Email'])
    for no, user in enumerate(user_data, start=1):
        writer.writerow([no, user.first_name, user.last_name, user.teamname, user.email])
    return response
