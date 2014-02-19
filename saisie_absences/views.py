from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from saisie_absences.forms import SaisieAbsencesForm

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
