groupe = Groupe()
groupe.ajouter(Etudiant("Amina", 12.0, 15.5))
groupe.ajouter(Etudiant("Brice", 10.0, 11.0))
groupe.ajouter(Etudiant("David", 14.0, 16.5))
print(f"Ex 12.5 - Moyenne générale : {groupe.moyenne_generale():.2f} / 20")

meilleur = groupe.etudiants[0]
for e in groupe.etudiants:
    if e.moyenne() > meilleur.moyenne():
        meilleur = e
print(f"Ex 12.5 - Meilleur étudiant : {meilleur.nom} ({meilleur.moyenne():.2f} / 20)")
