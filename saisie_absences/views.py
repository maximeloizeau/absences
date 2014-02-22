from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from saisie_absences.forms import SaisieAbsencesForm
from django.views.generic.list import ListView
from accounts.models import Absence, Etudiant, Enseignant, Matiere


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

class AbsencesView(ListView):
	model = Absence
	template_name = 'saisie_absences/list.html'
	context_object_name = 'absences'
	paginate_by = 20
	toJustify = False

	def get_queryset(self):
		user = Etudiant.objects.get(user=self.request.user)
		absences = Absence.objects.filter(etudiant=user).order_by('date')
		if self.toJustify:
			absences = absences.filter(justificatif=None)
		return absences

	def get(self, request):
		print(request.user.etudiant.toJustify)
		return render(self.request, 'saisie_absences/list.html', {
			'absences': self.get_queryset(),
			})
