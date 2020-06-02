# -*- coding: utf-8 -*-

# On importe la classe ExerciseFunction 
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


########## Etape 1
# On doit définir la "bonne" fonction répondant au problème

def carre(x):
    "calcule le carré de x"
    return x**2

########## Etape 2
# On doit fournir des valeurs à tester cette fonction carre,
# C'est arguments seront aussi utilisés pour la fonction
# trouvée par l'élève 
# Dans ce cas, on a défini 5 sorties, appelés "Args"
# donc dans la correction on aura 5 lignes de réponses attendues

# Pour que la fonction carre soit testée avec N exemples d'arguments
# il faut taper exo_exemple.example(N) dans le Notebook

inputs_test = [
    Args(5),
    Args(10),
    Args(0),
    Args(-5),
    Args(-10)
]

# The Args object takes eactly the arguments to be passed to the function
# so if the function was expecting 2 arguments, then I would have added
# Args(10, 12)
# or even
# Args(10, *(12, 13, 14))



########## Etape 3
# Enfin, on crée l'objet exercice
# REMARQUE : c'est le seul nom qui doit être importé de ce module
#
exo_exemple = ExerciseFunction(
    # Le premier argument est la "bonne" fonction
    # Il est recommandé d'utiliser le MEME nom que pour le notebook, pour
    # que lors de l'affichage des réponses, pour que le nom de la fonction
    # apparaisse aussi sinon, c'est le nom du fichier qui s'affiche
    carre,

    inputs_test,
    result_renderer=PPrintRenderer(width=20),
    font_size="75%",
    header_font_size="200%"
)

