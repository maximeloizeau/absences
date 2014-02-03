from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm

def register(request):
	template = 'accounts/register.html'
	if request.user.is_authenticated():
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
				user = auth.authenticate(username=user.username, password=request.POST['password'])
				auth.login(request, user)
				return HttpResponseRedirect(reverse('accounts:index'))
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
					return HttpResponseRedirect(reverse('accounts:index'))
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