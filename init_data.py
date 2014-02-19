from accounts.models import *
from django.contrib.auth.models import User, Group
from django.contrib import auth

user_ricoco = User.objects.create_user("ricoco", "ricoco@email.com", "aa", first_name="Eric", last_name="Ordelle")
user_pigeau = User.objects.create_user("pigeau", "pigeau@email.com", "aa", first_name="Antoine", last_name="Pigeau")
user_bidan = User.objects.create_user("bidan", "bidan@email.com", "aa", first_name="Marc", last_name="Bidan")
user_nachouki = User.objects.create_user("nachouki", "nachouki@email.com", "aa", first_name="MP", last_name="Nachouki")

user_loizeau = User.objects.create_user("loizeau", "loizeau@email.com", "aa", first_name="Maxime", last_name="Loizeau")
user_burgevin = User.objects.create_user("burgevin", "burgevin@email.com", "aa", first_name="Florian", last_name="Burgevin")
user_collet = User.objects.create_user("collet", "collet@email.com", "aa", first_name="Amaury", last_name="Collet")

user_buhe = User.objects.create_user("buhe", "buhe@email.com", "aa", first_name="Laurence", last_name="Buhe")


ricoco = Enseignant(user = User.objects.get(username="ricoco"))
pigeau = Enseignant(user = User.objects.get(username="pigeau"))
bidan = Enseignant(user = User.objects.get(username="bidan"))
nachouki = Enseignant(user = User.objects.get(username="nachouki"))


dpt_info = Departement(nom = "Informatique", directeur = ricoco)
dpt_te = Departement(nom = "Termique", directeur = bidan)
dpt_info.save()
dpt_te.save()

info3 = Annee(nom = "INFO3", dpt = dpt_info, responsable = nachouki)
info4 = Annee(nom = "INFO4", dpt = dpt_info, responsable = pigeau)
info3.save()
info4.save()

m1 = Matiere(nom = "BDD", annee = info4)
m2 = Matiere(nom = "IA", annee = info4)
m3 = Matiere(nom = "Archi", annee = info3)
m4 = Matiere(nom = "Algo", annee = info3)
m1.save()
m2.save()
m3.save()
m4.save()

loizeau = Etudiant(user = User.objects.get(username="loizeau"), annee = info4)
burgevin = Etudiant(user = User.objects.get(username="burgevin"), annee = info4)
collet = Etudiant(user = User.objects.get(username="collet"), annee = info4)

buhe = Secretaire(user = User.objects.get(username="buhe"))

g = Group.objects.get(pk=1)
g.user_set.add(user_loizeau)
g.user_set.add(user_burgevin)
g.user_set.add(user_collet)
g.save()

g = Group.objects.get(pk=2)
g.user_set.add(user_buhe)
g.save()

g = Group.objects.get(pk=3)
g.user_set.add(user_ricoco)
g.user_set.add(user_pigeau)
g.user_set.add(user_bidan)
g.user_set.add(user_nachouki)
g.save()

g = Group.objects.get(pk=4)
g.user_set.add(user_nachouki)
g.user_set.add(user_pigeau)
g.save()

g = Group.objects.get(pk=5)
g.user_set.add(user_ricoco)
g.user_set.add(user_bidan)
g.save()


loizeau.save()
burgevin.save()
collet.save()

buhe.save()

ricoco.save()
pigeau.save()
bidan.save()
nachouki.save()


m1.chargeDeMatiere.add(pigeau)
m2.chargeDeMatiere.add(ricoco)
m3.chargeDeMatiere.add(nachouki)
m4.chargeDeMatiere.add(pigeau)