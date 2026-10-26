"""Classe Livre"""


class Livre:
    """Représente un livre."""

    def __init__(self, titre, annee, genre):
        """Initialise un livre."""
        self.titre = titre
        self.annee = annee
        self.genre = genre

    def __str__(self):
        """Affichage du livre."""
        if self.genre:
            return f"{self.annee} [{self.genre}] {self.titre}"
        return f"{self.annee} {self.titre}"

    def __lt__(self, other):
        """Comparaison pour tri."""
        return (self.annee, self.genre, self.titre) < (
            other.annee, other.genre, other.titre
        )
