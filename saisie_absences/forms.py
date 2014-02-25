from accounts.models import Absence, Justificatif, Etudiant, Matiere
from django.forms import ModelForm, Form
from django import forms

class SaisieAbsencesForm(forms.Form):
	date = forms.DateTimeField(required=True, input_formats = ['%Y-%m-%d %H:%M', '%Y-%m-%d', '%d/%m/%Y %H:%M', '%d/%m/%Y',])
	matiere = forms.ModelChoiceField(queryset=Matiere.objects.all(), required=True)
	etudiants = forms.ModelMultipleChoiceField(queryset=Etudiant.objects.all(), required=True)


class SaisieJustificatifForm(forms.Form):
	motif = forms.CharField(max_length=200)
	fichier = forms.FileField(label= 'Selectionner le justificatif')
	etudiant = forms.ModelChoiceField(queryset = Etudiant.objects.all(), required = True)
	liste_absences = forms.ModelMultipleChoiceField(queryset=Absence.objects.all(), required=True)