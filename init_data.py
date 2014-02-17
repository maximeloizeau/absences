from accounts.models import *
from django.contrib.auth.models import User

ricoco = Enseignant(user = User.objects.get(username="ricoco"))
ricoco.save()
pigeau = Enseignant(user = User.objects.get(username="pigeau"))
pigeau.save()
dpt_info = Departement(nom = "Informatique", directeur = ricoco)
dpt_info.save()
info4 = Annee(nom = "INFO4", dpt = dpt_info, responsable = pigeau)
info4.save()
m = Matiere(nom = "BDD", annee = info4)
m.save()
m.chargeDeMatiere.add(pigeau)