"""Classe Bibliotheque."""

import json
import os
from biblio.livre import Livre

FICHIER = os.path.expanduser("~/.biblio.json")


class Bibliotheque:
    """Représente une bibliothèque."""

    def __init__(self):
        """Initialise la bibliothèque."""
        self.livres = []
        self.genres = []

    def ajoute_genre(self, genre):
        """Ajoute un genre."""
        self.genres.append(genre)

    def genre_existe(self, genre):
        """Teste si un genre existe."""
        return genre in self.genres

    def ajoute_livre(self, livre):
        """Ajoute un livre et trie."""
        self.livres.append(livre)
        self.livres.sort()

    def supprimer_livre(self, titre):
        """Supprime un livre."""
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                return True
        return False

    def supprimer_genre(self, genre):
        """Supprime un genre."""
        if genre not in self.genres:
            return False

        self.genres.remove(genre)

        for livre in self.livres:
            if livre.genre == genre:
                livre.genre = ""

        return True

    def sauvegarder(self):
        """Sauvegarde la bibliothèque."""
        try:
            data = {
                "genres": self.genres,
                "livres": [
                    {
                        "titre": livre.titre,
                        "annee": livre.annee,
                        "genre": livre.genre,
                    }
                    for livre in self.livres
                ],
            }

            with open(FICHIER, "w", encoding="utf-8") as fichier_json:
                json.dump(data, fichier_json)

        except OSError:
            print("Impossible de sauvegarder la bibliothèque")

    def charger(self):
        """Charge la bibliothèque."""
        try:
            with open(FICHIER, "r", encoding="utf-8") as fichier_json:
                data = json.load(fichier_json)

                self.genres = data.get("genres", [])
                self.livres = [
                    Livre(d["titre"], d["annee"], d["genre"])
                    for d in data.get("livres", [])
                ]

        except FileNotFoundError:
            # fichier absent bibliothèque vide
            pass
        except json.JSONDecodeError:
            print("Fichier JSON invalide")
        except OSError:
            print("Erreur lors du chargement")
