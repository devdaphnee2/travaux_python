def calculer_moyenne_classe(classe):
    total = 0
    for e in classe:
        total += e["note_cc"] * 0.4 + e["note_examen"] * 0.6
    return total / len(classe)


print(f"Ex 10.1 - Moyenne de la classe : {calculer_moyenne_classe(classe):.2f}")