from accounts.models import *
from django.contrib.auth.models import User
from django.contrib import auth

user_ricoco = User.objects.create_user("ricoco", "ricoco@email.com", "aa", first_name="Eric", last_name="Ordelle")
user_pig = User.objects.create_user("pig", "pig@email.com", "aa", first_name="Anthony", last_name="Pont")
ricoco = Enseignant(user = User.objects.get(username="ricoco"))
ricoco.save()
pig = Enseignant(user = User.objects.get(username="pig"))
pig.save()
dpt_info = Departement(nom = "Informatique", directeur = ricoco)
dpt_info.save()
info4 = Annee(nom = "INFO4", dpt = dpt_info, responsable = pig)
info4.save()
m = Matiere(nom = "BDD", annee = info4)
m.save()
m.chargeDeMatiere.add(pig)