bulletins = [(10.5, 17.5, 14.2), (8.0, 15.0, 11.5), (12.0, 18.0, 15.0)]
for i, (note_min, note_max, moy) in enumerate(bulletins, start=1):
    print(f"Ex 8.3 - Étudiant {i} : écart = {note_max - note_min:.2f}")

# Exercice 4 : .get() avec valeur par défaut
etudiant = {"nom": "Brice", "age": 21, "moyenne": 12.5}
print("Ex 8.4 - Mention :", etudiant.get("mention", "aucune"))
