from django.contrib.auth.models import Group
from django import forms
from accounts.models import Annee, Departement

class LoginForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	login = forms.CharField(max_length=100, label="Nom d'utilisateur")
	first_name = forms.CharField(max_length=100, label="Prénom")
	last_name = forms.CharField(max_length=100, label="Nom")
	email = forms.EmailField()
	role = forms.ModelChoiceField(widget=forms.Select(), queryset=Group.objects.all())
	annee = forms.ModelChoiceField(widget=forms.Select(), queryset=Annee.objects.all(), required = False, label="Année d'étude")
	dpt = forms.ModelChoiceField(widget=forms.Select(), queryset=Departement.objects.all(), required = False, label="Responsable de département")
	respo_annee = forms.ModelChoiceField(widget=forms.Select(), queryset=Annee.objects.all(), required = False, label="Responsable d'année")
	password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
	password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmation du mot de passe")