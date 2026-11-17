filieres = ["Génie Logiciel", "Réseaux", "Gestion", "Marketing", "Logistique"]
effectifs = [42, 35, 28, 31, 24]
plt.figure(figsize=(9, 4))
plt.bar(filieres, effectifs, color="#2e75b6")
plt.title("Effectifs par filière")
plt.xlabel("Filière")
plt.ylabel("Nombre d'étudiants")
afficher("ex11_3.png")