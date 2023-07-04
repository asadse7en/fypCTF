from django import forms
from . import models

category_list = [
	('Cryptography','Cryptography'),
	('Forensics','Forensics'),
	('Pwning','Pwning'),
	('Reverse Engineering','Reverse Engineering'),
	('Stegnography','Stegnography'),
	('Web','Web'),
	('OSINT','OSINT'),
	('Misc','Misc')

]

level = [
	('EASY','EASY'),
	('MEDIUM','MEDIUM'),
	('HARD','HARD')
]
class AddChallengeForm(forms.ModelForm) :
	name = forms.CharField(max_length=250, label="Challenge Name *", widget=forms.TextInput(attrs={'placeholder':'Challenge Name','class':'form-control'}))
	category = forms.CharField(widget=forms.Select(choices=category_list, attrs={'class':'form-control'}), label="Challenge Category *")
	difficulty = forms.CharField(widget=forms.Select(choices=level, attrs={'class':'form-control'}), label="Difficulty")
	description = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={'placeholder':'Challenge Description', 'class':'form-control','required':'false'}), label="Challenge Description *", required=False)
	hints = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder':'Challenge Hints', 'class':'form-control'}), label="Challenge Hints", required=False)
	points = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Challenge Points *")
	flag = forms.CharField(max_length=500, label="Challenge Flag *", widget=forms.TextInput(attrs={'placeholder':'Challenge Flag','class':'form-control'}))
	author_name = forms.CharField(max_length=250, label="Challenge Author Name *", widget=forms.TextInput(attrs={'placeholder':'Challenge Author Name','class':'form-control'}))
	author_link = forms.URLField(max_length=250, label="Challenge Author Link", widget=forms.URLInput(attrs={'placeholder':'Challenge Author Link','class':'form-control'}), required=False)

	class Meta :
		model = models.Challenges
		fields = ["name","category", "difficulty", "description", "hints", "points", "flag", "author_name", "author_link"]


class DeleteChallengesForm(forms.Form):
    challenge_id = forms.CharField(label="Challenge ID to delete", widget=forms.TextInput(attrs={'class':'form-control'}))
