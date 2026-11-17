class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"Je suis {self.nom}, délégué de la filière {self.filiere}."