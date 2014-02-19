from accounts.models import Absence
from django.forms import ModelForm

class SaisieAbsencesForm(ModelForm):
	class Meta:
		model = Absence
		fields = ('date', 'matiere', 'etudiant')