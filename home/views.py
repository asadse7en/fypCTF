from django.shortcuts import render, redirect
from fypCTF.config import name, start_time, end_time, tags, allowed_categories
from django.db.models import Sum
from challenges.models import Challenges, ChallengesSolvedBy
from accounts.models import Teams


def home(request) :
	return render(request, 'home.html', {'name': name(), 'start_time':start_time(), 'end_time':end_time(), 'tags':tags(), 'allowed':allowed_categories()})

def manage(request) :
        total_challenges = Challenges.total_challenges()
        total_solves = ChallengesSolvedBy.objects.count()
        username_most_solves, most_solve_count = Challenges.user_with_most_solves()
        username_least_solves, least_solve_count = Challenges.user_with_least_solves()
        total_participants = Teams.total_participants()
        highest_points_possible =  Challenges.objects.aggregate(total_points=Sum('points')).get('total_points')
        overall_total_points = ChallengesSolvedBy.objects.aggregate(total_points=Sum('points')).get('total_points')
        most_solved_challenge, most_solved_count = Challenges.challenge_with_most_solves()
        least_solved_challenge, least_solved_count = Challenges.challenge_with_least_solves()
        most_first_blood_user, most_first_blood_count = ChallengesSolvedBy.most_first_blood()




        context = {
        'total_challenges': total_challenges,
        'total_solves': total_solves,
        'username_most_solves': username_most_solves,
        'most_solve_count': most_solve_count,
        'username_least_solves': username_least_solves,
        'least_solve_count': least_solve_count,
        'total_participants': total_participants,
        'highest_points_possible': highest_points_possible,
        'most_solved_challenge': most_solved_challenge,
        'most_solved_count': most_solved_count,
        'least_solved_challenge': least_solved_challenge,
        'least_solved_count': least_solved_count,
        'overall_total_points': overall_total_points,
        'most_first_blood_user': most_first_blood_user,
        'most_first_blood_count': most_first_blood_count,
        'name': name()
    }
        if request.user.is_superuser :
            return render(request, 'manage.html', context)
        else :
            return redirect("/")

def resources(request) :
	return render(request, 'resources.html')



import csv
from django.http import HttpResponse
from accounts.models import Teams
from challenges.models import Challenges as challs

def download_scoreboard(request):
    scoreboard_data = Teams.objects.order_by("-points")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'
    writer = csv.writer(response)
    writer.writerow(['#', 'User Name', 'Affiliation', 'Points'])
    for rank, entry in enumerate(scoreboard_data, start=1):
        writer.writerow([rank, entry.teamname, entry.affiliation, entry.points])

    if request.user.is_superuser :
            return response
    else:
        return redirect("/")
    
def download_user_data(request):
    user_data = Teams.objects.all().order_by('teamname')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['#', 'First Name', 'Last Name', 'Username', 'Affiliation', 'Email'])
    for no, user in enumerate(user_data, start=1):
        writer.writerow([no, user.first_name, user.last_name, user.teamname, user.affiliation, user.email])
    
    if request.user.is_superuser :
            return response
    else:
        return redirect("/")



def download_challenges_data(request):
    data = challs.objects.all().order_by('category')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="challenges.csv"'
    '''writer = csv.writer(response)
    writer.writerow(['#', 'Name', 'ID', 'Category', 'Difficulty', 'Description', 'Hints', 'Points', 'Flag', 'Author Name', 'Solve Count'])
    for no, Challenges in enumerate(data, start=1):
        writer.writerow([no, Challenges.name, Challenges.challenge_id, Challenges.category, Challenges.difficulty, Challenges.description, Challenges.hints, Challenges.points, Challenges.flag, Challenges.author_name, Challenges.solve_count])
    '''
    if request.user.is_superuser :
            return response
    else:
        return redirect("/")

def solves(request):
    solves_list = ChallengesSolvedBy.objects.order_by("-time")
    return render(request, 'solves.html', {'solves_list': solves_list})


def firstblood(request):
    solves_list = ChallengesSolvedBy.objects.filter(first_blood=True).order_by("-time")
    return render(request, 'firstblood.html', {'solves_list': solves_list})



from django.http import JsonResponse
import json

def scoreboard_json(request):
    standings = []
    teams = Teams.objects.order_by('-points')

    for index, team in enumerate(teams, start=1):
        standing = {
            "pos": index,
            "team": team.teamname,
            "score": team.points,
        }
        standings.append(standing)

    data = {"standings": standings}
    json_data = json.dumps(data, indent=4)
    if request.user.is_superuser :
            return HttpResponse(json_data, content_type='application/json')
    else:
        return redirect("/")



def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)