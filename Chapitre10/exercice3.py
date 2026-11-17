def statistiques(notes):
    return sum(notes) / len(notes), min(notes), max(notes)


moy, mini, maxi = statistiques([12.5, 14.0, 13.5, 16.0, 15.5])
print(f"Ex 10.3 - Moyenne : {moy:.2f} | Min : {mini} | Max : {maxi}")