from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from accounts.forms import LoginForm, RegisterForm
from accounts.models import Enseignant, Departement, Annee, Secretaire, Etudiant

@login_required
def register(request):
	template = 'accounts/register.html'
	if not request.user.groups.filter(pk=2).exists():
		return HttpResponseRedirect(reverse('accounts:index'))
	else:
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				if User.objects.filter(username=request.POST['login']).count():
					return render(request, template, {
						'form': form,
						'error': 'Nom d\'utilisateur déjà utilisé.',
					})
				# TODO : try/catch création utilisateur
				user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
				if request.POST['role'] == "1":
					utilisateur = Etudiant(user = user, annee = Annee.objects.get(pk=request.POST['annee']))
				elif request.POST['role'] == "2":
					utilisateur = Secretaire(user = user)
				elif request.POST['role'] == "3":
					utilisateur = Enseignant(user = user)
				else:
					return render(request, template, {
						'form': form,
						'error': 'Type d\'utilisateur invalide',
					})
					user.delete()

				utilisateur.save()

				# Ajout utilisateur à un groupe
				g = Group.objects.get(pk=request.POST['role'])
				g.user_set.add(user)
				g.save()

				if isinstance(utilisateur, Enseignant):
					if request.POST['respo_annee']:
						g = Group.objects.get(pk=5)
						g.user_set.add(user)
						g.save()
						a = Annee.objects.get(pk=request.POST['respo_annee'])
						a.responsable = utilisateur
						a.save()
					elif request.POST['dpt']:
						g = Group.objects.get(pk=4)
						g.user_set.add(user)
						g.save()
						d = Departement.objects.get(pk=request.POST['dpt'])
						d.directeur = utilisateur
						d.save()


				# Connexion utilisateur
				# user = auth.authenticate(username=user.username, password=request.POST['password'])
				# auth.login(request, user)
				return HttpResponseRedirect(reverse('accounts:userlist'))
			else:
				return render(request, template, {
					'form': form,
					'error': 'Veillez à bien renseigner tous les champs.',
				})
		else:
			form = RegisterForm()

	return render(request, template, {
		'form': form,
	})

def login(request):
	template = 'accounts/login.html'
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('accounts:index'))
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = request.POST['login']
				password = request.POST['password']
				user = auth.authenticate(username=username, password=password)
				if user is not None:
					auth.login(request, user)					
					return HttpResponseRedirect(reverse('saisie:index'))
				else:
					return render(request, template, {
						'form': form,
						'error': 'La connexion a échouée.',
					})
			else:
				return render(request, template, {
					'form': form,
					'error': 'Veuillez remplir tous les champs correctement.',
				})
		else:
			form = LoginForm()

	return render(request, template, {
		'form': form,
	})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def index(request):
	return render(request, 'accounts/index.html', {
		'user': request.user,
	})

@login_required
def userlist(request):
	return render(request, 'accounts/list.html', {
		'list': User.objects.all(),
	})