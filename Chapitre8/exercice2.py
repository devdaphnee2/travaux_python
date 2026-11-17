classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
    {"nom": "Chloé", "note_cc": 14.0, "note_examen": 16.0},
]
total = 0
for e in classe:
    moy = e["note_cc"] * 0.4 + e["note_examen"] * 0.6
    total += moy
    print(f"Ex 8.2 - {e['nom']} : {moy:.2f} / 20")
print(f"Ex 8.2 - Moyenne générale de la classe : {total / len(classe):.2f} / 20")