sns.set_theme(style="whitegrid")
notes_classe = [8, 9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 17, 18]
plt.figure(figsize=(8, 4.5))
sns.histplot(notes_classe, bins=10, kde=True, color="#2e75b6")
plt.title("Distribution des notes de la classe")
plt.xlabel("Note (/20)")
afficher("ex11_5.png")