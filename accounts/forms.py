from django.contrib.auth.models import Group
from django import forms
from accounts.models import Annee, Departement

class LoginForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	login = forms.CharField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	role = forms.ModelChoiceField(widget=forms.Select(), queryset=Group.objects.all())
	annee = forms.ModelChoiceField(widget=forms.Select(), queryset=Annee.objects.all(), required = False)
	dpt = forms.ModelChoiceField(widget=forms.Select(), queryset=Departement.objects.all(), required = False)
	respo_annee = forms.ModelChoiceField(widget=forms.Select(), queryset=Annee.objects.all(), required = False)
	password = forms.CharField(widget=forms.PasswordInput)