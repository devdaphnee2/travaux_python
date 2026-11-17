etudiants_releve = [("Amina", 12, 14.75), ("Brice", 10, 13.5)]
print("Ex 3.3 - Relevé :")
for nom, credits, note in etudiants_releve:
    print(f"{nom:<6}{credits:>5}{note:>10.2f} / 20")