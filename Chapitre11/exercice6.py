random.seed(1)
base = [random.uniform(8, 17) for _ in range(10)]
notes_df = pd.DataFrame({
    "Maths": [round(b + random.uniform(-2, 2), 1) for b in base],
    "Algo": [round(b + random.uniform(-2, 2), 1) for b in base],
    "Réseaux": [round(b + random.uniform(-3, 3), 1) for b in base],
})
corr = notes_df.corr()
print(corr)
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", vmin=0, vmax=1, square=True)
plt.title("Corrélation entre les notes des matières")
afficher("ex11_6.png")