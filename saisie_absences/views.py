from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, 'saisie_absences/index.html', {
		'user': request.user,
		'is_etudiant': request.user.groups.filter(pk=1).exists(),
		'is_secretaire': request.user.groups.filter(pk=2).exists(),
		'is_enseignant': request.user.groups.filter(pk=3).exists(),
		'is_reponsable': request.user.groups.filter(pk=4).exists(),
		'is_directeur': request.user.groups.filter(pk=5).exists(),
	})
