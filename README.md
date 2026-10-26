# R208 – Analyse et traitement des données : paquet `biblio`

Petit paquet Python pour gérer une bibliothèque (livres et genres) en ligne de commande, avec sauvegarde/chargement des données.

## Structure
```
biblio/
  __init__.py       # version et e-mail de support
  bibliotheque.py   # classe Bibliotheque (genres, livres, sauvegarde/chargement)
  commandes.py      # fonctions des commandes du menu
  livre.py          # classe Livre
bibliodb            # script principal (interface en ligne de commande)
setup.py            # installation du paquet avec setuptools
```

## Installation et lancement
```bash
pip install .
bibliodb
```

## Commandes du menu
| Commande | Action |
|---|---|
| `M` | Afficher le menu |
| `NG` / `NL` | Nouveau genre / nouveau livre |
| `LG` / `LL` | Lister les genres / les livres |
| `SG` / `SL` | Supprimer un genre / un livre |
| `Q` | Quitter |

**Mots-clés :** Python, POO, packaging (`setup.py`), persistance des données.
