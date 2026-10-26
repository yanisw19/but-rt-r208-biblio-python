"""Commandes utilisateur."""

from biblio.livre import Livre


def affiche_menu():
    """Affiche le menu."""
    print("****************************************")
    print("Menu principal")
    print("[M] Menu principal")
    print("[LG] Liste des Genres")
    print("[LL] Liste des Livres")
    print("[NG] Nouveau Genre")
    print("[NL] Nouveau Livre")
    print("[SG] Suppression d'un Genre")
    print("[SL] Suppression d'un Livre")
    print("[Q] Quitter le programme")
    print("****************************************")


def nouveau_genre(biblio):
    """Ajoute un genre."""
    genre = input("> Entrez le nom du genre : ")

    if biblio.genre_existe(genre):
        print("Ce genre existe déjà!")
    else:
        biblio.ajoute_genre(genre)
        print(f"Le genre {genre} a été créé.")


def nouveau_livre(biblio):
    """Ajoute un livre."""
    titre = input("> Entrez le titre du livre : ")
    annee = int(input("> Entrez l'année : "))

    while True:
        genre = input("> Entrez le genre : ")
        if genre == "" or biblio.genre_existe(genre):
            break
        print("Ce genre n'existe pas!")

    livre = Livre(titre, annee, genre)
    biblio.ajoute_livre(livre)

    print(f'Le livre "{titre}" a été créé.')


def afficher_livres(biblio):
    """Affiche la liste des livres."""
    print(f"{len(biblio.livres)} livre(s) trouvé(s)")
    for livre in biblio.livres:
        print(livre)

#EXO7

def liste_genres(biblio):
    """Affiche les genres."""
    for genre in biblio.genres:
        count = sum(1 for l in biblio.livres if l.genre == genre)
        print(f"{genre}: {count} livre(s)")

    count = sum(1 for l in biblio.livres if l.genre == "")
    if count > 0:
        print(f"sans genre: {count} livre(s)")


def supprimer_livre(biblio):
    """Supprime un livre."""
    titre = input("> Entrez le titre du livre : ")

    if biblio.supprimer_livre(titre):
        print(f'Le livre "{titre}" a été supprimé.')
    else:
        print("Ce livre n'existe pas!")


def supprimer_genre(biblio):
    """Supprime un genre."""
    genre = input("> Entrez le nom du genre : ")

    if biblio.supprimer_genre(genre):
        print(f"Le genre {genre} a été supprimé.")
    else:
        print("Ce genre n'existe pas!")
