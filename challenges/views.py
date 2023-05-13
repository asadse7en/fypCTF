from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import models
from accounts import models as accounts_models
from fypCTF.config import allowed_categories, show_challenges
from . import forms
from django.contrib import messages
from django.utils import timezone






class PassInsideView() :
	name = ''
	challenge_id = ''
	category = ''
	difficulty = ''
	description = ''
	hints = ''
	points = ''
	file = ''
	flag = ''
	author_name = ''
	author_link = ''
	solve_count = ''

	def __init__(self, name, challenge_id, category, difficulty,description, hints, points, file, flag, author_name, author_link, solve_count) :
		self.name = name
		self.challenge_id = challenge_id
		self.category = category
		self.description = description
		self.hints = hints
		self.points = points
		self.file = file
		self.flag = flag
		self.author_name = author_name
		self.author_link = author_link
		self.solve_count = solve_count
		self.difficulty = difficulty

def assignID(a) :
	return a.lower().replace(' ','_')



@login_required(login_url="/accounts/login/")
def index(request) :
		challenge = models.Challenges.objects.order_by("points")
		challenge_info_stego_object = []
		challenge_info_for_object = []
		challenge_info_re_object = []
		challenge_info_pwn_object = []
		challenge_info_web_object = []
		challenge_info_crypto_object = []
		challenge_info_osint_object = []
		challenge_info_misc_object = []

		for c in challenge :
			if c.category == 'Stegnography' :
				s = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_stego_object.append(s)
			elif c.category == 'Reverse Engineering' :
				re = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_re_object.append(re)
			elif c.category == 'Forensics' :
				f = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_for_object.append(f)
			elif c.category == 'Pwning' :
				p = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_pwn_object.append(p)
			elif c.category == 'Web' :
				w = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_web_object.append(w)
			elif c.category == 'Cryptography' :
				cy = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_crypto_object.append(cy)
			elif c.category == 'OSINT' :
				o = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_osint_object.append(o)
			elif c.category == 'Misc' :
				mc = PassInsideView(c.name, assignID(c.name), c.category, c.difficulty, c.description, c.hints, c.points, c.file, c.flag, c.author_name, c.author_link, c.solve_count)
				challenge_info_misc_object.append(mc)

		solved_challenges_by_user = []
		try :
			fc = models.ChallengesSolvedBy.objects.filter(user_name=request.user)
			for f in fc :
				solved_challenges_by_user.append(f.challenge_id)
		except :
			pass

		return render(request, 'challenges.html', {
			'data_stego':challenge_info_stego_object,
			'data_for':challenge_info_for_object,
			'data_re':challenge_info_re_object,
			'data_pwn':challenge_info_pwn_object,
			'data_web':challenge_info_web_object,
			'data_crypto':challenge_info_crypto_object,
			'data_osint':challenge_info_osint_object,
			'data_misc':challenge_info_misc_object,
			'user_solved':solved_challenges_by_user,
			'allowed':allowed_categories,
			'show_challenges':show_challenges,
	})


@login_required(login_url="/accounts/login/")
def flagsubmit(request):
    if request.method == 'POST':
        # get flag and challenge info
        flag_submit = ''
        flag_submit_id = ''
        x = ''
        for k in request.POST:
            if k == 'submit':
                continue
            if k == 'csrfmiddlewaretoken':
                continue
            else:
                x = k
        flag_submit = request.POST[x]
        flag_submit_id = x[:-5]
        flag = models.Challenges.objects.get(challenge_id=flag_submit_id).flag
        points = models.Challenges.objects.get(challenge_id=flag_submit_id).points
        solve_count = models.Challenges.objects.get(challenge_id=flag_submit_id).solve_count

        if flag == flag_submit and not request.user.is_superuser:
            # check if challenge has already been solved by the user
            fc = models.ChallengesSolvedBy.objects.filter(user_name=request.user)
            obs = []
            for k in fc:
                obs.append(k.challenge_id)

            # update solve count if challenge has not been solved before
            if flag_submit_id not in obs:
                fr = models.ChallengesSolvedBy(challenge_id=flag_submit_id, user_name=request.user, points=points)
                fr.save()
                models.Challenges.objects.filter(challenge_id=flag_submit_id).update(solve_count=solve_count+1)
                initial_points = accounts_models.Teams.objects.get(teamname=request.user).points
                updated_points = initial_points + points
                accounts_models.Teams.objects.filter(teamname=request.user).update(points=updated_points)
                response = '<div id="flag_correct"><p>CORRECT</p></div>'
            else:
                response = '<div id="flag_already"><p>ALREADY SUBMITTED</p></div>'
        elif request.user.is_superuser:
            response = '<div id="flag_already"><p>Logged in as Admin</p></div>'
        else:
            response = '<div id="flag_incorrect"><p>INCORRECT</p></div>'

    return HttpResponse(response)


@login_required(login_url="/accounts/login/")
def addchallenges(request) :
	
	if request.user.is_superuser :
		if request.method == 'POST' :
			success = 0
			form = forms.AddChallengeForm(request.POST, request.FILES)
			if form.is_valid() :
				success = 1
				print(request.FILES)
				if request.FILES :
					i = models.Challenges(file=request.FILES['file'], 
						name=request.POST['name'], 
						category=request.POST['category'], 
						difficulty=request.POST['difficulty'], 
						description=request.POST['description'], 
						hints=request.POST['hints'], 
						points=request.POST['points'],
						challenge_id=assignID(request.POST['name']),
						flag=request.POST['flag'], 
						author_name=request.POST['author_name'],
						author_link=request.POST['author_link'])
					i.save()
				else :
					i = models.Challenges( 
						name=request.POST['name'], 
						category=request.POST['category'], 
						difficulty=request.POST['difficulty'], 
						description=request.POST['description'], 
						hints=request.POST['hints'], 
						points=request.POST['points'],
						challenge_id=assignID(request.POST['name']),
						flag=request.POST['flag'], 
						author_name=request.POST['author_name'],
						author_link=request.POST['author_link'])
					i.save()
				return render(request, 'addchallenges.html', {'form':form,'success':success})
		else :
			form = forms.AddChallengeForm()

		return render(request, 'addchallenges.html', {'form':form})
	
	else :
		return redirect("/")
	

@login_required(login_url="/accounts/login/")
def deletechallenges(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = forms.DeleteChallengesForm(request.POST)
            if form.is_valid():
                challenge_id = form.cleaned_data['challenge_id']
                challenge = models.Challenges.objects.get(pk=challenge_id)
                challenge.delete()
                messages.success(request, "Challenge deleted successfully!")
                return redirect('/admin/')
        else:
            form = forms.DeleteChallengesForm()
        return render(request, 'deletechallenges.html', {'form': form})
    else:
        return redirect("/")
