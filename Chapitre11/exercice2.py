moyenne_glissante = []
for i in range(len(notes)):
    if i < 2:
        moyenne_glissante.append(None)
    else:
        moyenne_glissante.append((notes[i] + notes[i - 1] + notes[i - 2]) / 3)

plt.figure(figsize=(9, 4.5))
plt.plot(evaluations, notes, label="Notes", color="#1f4e79")
plt.plot(evaluations, moyenne_glissante, label="Moyenne glissante (3)", color="#e07a1f", linestyle="--")
plt.title("Notes et moyenne glissante")
plt.xlabel("Évaluation")
plt.ylabel("Note (/20)")
plt.legend()
plt.grid(alpha=0.3)
afficher("ex11_2.png")