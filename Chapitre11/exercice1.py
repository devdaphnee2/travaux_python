def evaluer_note(note):
    if note < 10:
        return "ÉCHEC"
    elif note >= 14:
        return "MENTION"
    return "PASSABLE"


def compter_reussites(notes):
    return sum(1 for n in notes if n >= 10)


notes = [8, 12, 15, 17, 10, 6]
for note in notes:
    print(f"Ex 10.4 - {note} : {evaluer_note(note)}")
print("Ex 10.4 - Nombre de réussites :", compter_reussites(notes))