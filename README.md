# E3FI - PR2 : Projet de Python

L’objectif du mini projet est d’éclairer un sujet d’intérêt public (météo, environnement, politique, vie publique, finance, transports, culture, santé, sport, économie, agriculture, écologie, etc…) que vous choisissez librement. Vous utiliserez des données publiques Open Data, accessibles et non modifiées.

Notation
https://perso.esiee.fr/~courivad/3IPR2/miniprojetdata.html

Après clonage du dépôt et à l’exécution de main.py :

- le code ne doit pas produire de warnings dans la console ;
- le dashboard ne doit pas comporter pas d’erreur de call back.

Diviser en sub fichier

## USER GUIDE

### INSTALLATION

1. Clonez ce dépôt dans votre environnement local :

   git clone https://github.com/71m07h33/E3-PR2-Miniprojet.git

2. Accédez au répertoire du projet :

   cd E3-PR2-Miniprojet

3. Installez les dépendances nécessaires :

   pip install plotly dash pandas

### UTILISATION

1. Ouvrez le projet dans un IDE (ex : Visual Studio Code)

2. Éxecuter le fichier main.py dans une invite de commande. Le fichier va ainsi installer les fichiers de données necessaires

3. Ouvrez un navigateur web et "Ctrl + click gauche" sur le lien donné dans l'invite de commande

   http://127.0.0.1:8050/

Vous pouvez maintenant accéder au Dashboard.

ELEMENT 1 : HISTOGRAMME COMPOSITION DES SPORTS EN FONCTIONS DE L'AGE ET DU SEXE

L'utilisateur choisis : - Le sport - La localisation - L'année (Entre 2017 et 2019)

=> On génère un histogramme avec le nombre de licenciés dans un sport dans une région en fonction de l'âge (Homme, Femme pour chaque catégorie d'âge)
=> Générer une animation à travers les années

ELEMENT 2 : CARTE DYNAMIQUE CONCENTRATION SPORTIF

L'utilisateur choisis : - Le sport (Si aucun sport n'est choisis, on prendra le nombre totale de licenciés sur tout les sports) - L'information (Le nombre de clubs ou le nombre de licenciés ? (radio))

L'utilisateur peut filtrer : - En fonction de l'age - En fonction du sexe

=> On génère une cartre chaud/froid de la france avec la concentration dans un sport dans chaque région
=> Générer une animation à travers les années

ELEMENT 2 : CARTE DYNAMIQUE LE SPORT LE PLUS POPULAIRE PAR REGION

L'utilisateur choisis : - L'année - La catégorie - La sexe

=> On génère une cartre avec pour chaque région de france le sport le plus populaire

ELEMENT 3 : CAMEMBERT DES ACTIVITÉS

L'utilisateur choisis :

- une commune

=> on génère un camembert représentant l'ensemble des activités des Fédérations de la commune

A FAIRE :

Faire plusieurs pages
Rendre le tout jolie avec du css
Stats sur france et sport en général (trop de calcul ?)
Supprimer lignes sports problématiques

ELEMENT 3 : EVOLUTION

-> Evolution de de la partique du sport sur 3 ans sur la région
