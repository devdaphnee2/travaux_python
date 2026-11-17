etudiants = [
    ["Amina", 19, 14.5],
    ["Brice", 21, 12.0],
    ["Chloé", 20, 16.5],
]
print("Ex 4.4 - Nom du 2e étudiant :", etudiants[1][0])
moyenne_generale = sum(e[2] for e in etudiants) / len(etudiants)
print(f"Ex 4.4 - Moyenne générale : {moyenne_generale:.2f}")