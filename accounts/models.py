from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Utilisateur(models.Model):
	user = models.OneToOneField(User)

	class Meta:
		abstract = True

class Enseignant(Utilisateur):
	pass

class Departement(models.Model):
	nom = models.CharField(max_length=200)
	directeur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null = True)

	def __str__(self):
		return self.nom

class Annee(models.Model):
	nom = models.CharField(max_length=200)
	dpt = models.ForeignKey(Departement)
	responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null = True)

	def __str__(self):
		return self.nom

class Matiere(models.Model):
	nom = models.CharField(max_length=200)
	annee = models.ForeignKey(Annee)
	chargeDeMatiere = models.ManyToManyField(Enseignant)

	def __str__(self):
		return self.nom

class Etudiant(Utilisateur):
	annee = models.ForeignKey(Annee, on_delete=models.SET_NULL, null = True)

class Secretaire(Utilisateur):
	pass

class Absence(models.Model):
	date = models.DateTimeField()
	matiere = models.ForeignKey(Matiere)
	etudiant = models.ForeignKey(Etudiant)

class Justificatif(models.Model):
	dateDebut = models.DateTimeField()
	dateFin = models.DateTimeField()
	fichier = models.CharField(max_length=200)
	etudiant = models.ForeignKey(Etudiant)

admin.site.register(Etudiant)
admin.site.register(Enseignant)
admin.site.register(Secretaire)
admin.site.register(Departement)
admin.site.register(Annee)
admin.site.register(Matiere)
admin.site.register(Absence)
admin.site.register(Justificatif)