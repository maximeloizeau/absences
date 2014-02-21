from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from accounts.models import Justificatif, Absence, Etudiant
from django.contrib.auth.decorators import login_required
from saisie_absences.forms import SaisieAbsencesForm, SaisieJustificatifForm, StudentForm

@login_required
def index(request):
	return render(request, 'saisie_absences/index.html', {
		'user': request.user
	})

@login_required
def saisie(request):
	if request.user.groups.filter(pk=3).exists():
		template = 'saisie_absences/saisie.html'

		if request.method == 'POST':
			form = SaisieAbsencesForm(request.POST)
			if form.is_valid():
				form.save()
				form = SaisieAbsencesForm()
				return render(request, template, {
					'form': form,
					'info' : 'Absence enregistrée.'
				})
			else:
				return render(request, template, {
					'form': form,
					'error': 'Veuillez remplir tous les champs correctement.',
				})
		else:
			form = SaisieAbsencesForm()
			return render(request, template,{
				'form': form
			})
		

	else:
		return HttpResponseRedirect(reverse('saisie:index'))

@login_required
def justificatif(request):
	if request.user.groups.filter(pk=2).exists():
		template = 'saisie_absences/justificatif.html'

		if request.method == 'POST':

			form = StudentForm(request.POST)
			if form.is_valid():

				absences = request.POST.getlist('liste_absences')

				justif = Justificatif(motif = request.POST['motif'], fichier = request.POST['fichier'], etudiant =  Etudiant.objects.get(pk=request.POST['eleve']))
				justif.save()

				for i in absences:
					if ( request.POST['eleve'] == Absence.objects.get(pk = i).etudiant.pk.__str__()):
						absence = Absence.objects.get(pk = i)
						absence.justificatif = justif
						absence.save()


				form = StudentForm()
				return render(request, template, {
					'form': form,
					'info': 'Justificatif enregistré.'
				})
			else:
				return render(request, template, {
					'form': form,
					'error': 'Veuillez remplir tous les champs correctement.',
				})
		else:

			form = StudentForm()
			return render(request, template,{
				'form': form
			})

	else:
		return HttpResponseRedirect(reverse('saisie:index'))