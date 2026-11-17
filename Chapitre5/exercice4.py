notes_cc = [10, 12, 9, 14]
notes_examen = [12, 11, 13, 14]
for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print(f"Ex 5.4 - Étudiant {i + 1} : PROGRESSION")
    else:
        print(f"Ex 5.4 - Étudiant {i + 1} : PAS DE PROGRESSION")