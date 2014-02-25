from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Count
from datetime import date, timedelta
from accounts.models import Absence, Etudiant, Enseignant, Matiere, Annee, Departement, Justificatif
from saisie_absences.forms import SaisieAbsencesForm, SaisieJustificatifForm

@login_required
def index(request):
	if request.user.groups.filter(pk=4):
		alert = Absence.objects.filter(date__gt=date.today()-timedelta(days=3*365/12)).annotate(nb_absences=Count('etudiant'))
	if request.user.groups.filter(pk=5):
		pass
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
				etudiants = request.POST.getlist('etudiants')

				for etu in etudiants:
					absence = Absence(date=request.POST['date'], matiere=Matiere.objects.get(pk=request.POST['matiere']), etudiant=Etudiant.objects.get(pk=etu))
					absence.save()

				return HttpResponseRedirect(reverse('saisie:list'))
			else:
				return render(request, template, {
					'form': form,
					'error': 'Veuillez remplir tous les champs correctement.',
				})
		else:
			form = SaisieAbsencesForm()
			form.fields['matiere'].queryset = Matiere.objects.filter(chargeDeMatiere__id=request.user.enseignant.id)
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

			form = SaisieJustificatifForm(request.POST, request.FILES)
			if form.is_valid():

				absences = request.POST.getlist('liste_absences')

				justif = Justificatif(motif = request.POST['motif'], fichier = request.FILES['fichier'], etudiant =  Etudiant.objects.get(pk=request.POST['eleve']))
				justif.save()

				for i in absences:
					if ( request.POST['eleve'] == Absence.objects.get(pk = i).etudiant.pk.__str__()):
						absence = Absence.objects.get(pk = i)
						absence.justificatif = justif
						absence.save()


				form = SaisieJustificatifForm()
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

			form = SaisieJustificatifForm()
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
	year = False
	department = False

	def get_queryset(self, arg):
		if self.request.user.groups.filter(pk=1).exists():
			user = Etudiant.objects.get(user=self.request.user)
			absences = Absence.objects.filter(etudiant=user).order_by('date')
		elif self.request.user.groups.filter(pk=2).exists():
			absences = Absence.objects.all().order_by('date')
		elif self.request.user.groups.filter(pk=3).exists():
			if self.request.user.groups.filter(pk=5).exists() and self.department:
				absences = Absence.objects.filter(matiere__in=Matiere.objects.filter(annee__in=Annee.objects.filter(dpt__in=Departement.objects.filter(directeur_id=self.request.user.enseignant.id))))
			elif self.request.user.groups.filter(pk=4).exists() and self.year:
				absences = Absence.objects.filter(matiere__in=Matiere.objects.filter(annee=Annee.objects.filter(responsable_id=self.request.user.enseignant.id)))
			else:
				absences = Absence.objects.filter(matiere__in=Matiere.objects.filter(chargeDeMatiere__id=self.request.user.enseignant.id)).order_by('-date')
			
			self.template_name = 'saisie_absences/list_enseignant.html'

		if self.toJustify:
			absences = absences.filter(justificatif=None)

		return absences

	def get(self, request, arg=None):
		absences = self.get_queryset(arg)
		return render(self.request, self.template_name, {
			'absences': absences,
			})