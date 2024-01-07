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

   $ python -m pip install -r requirements.txt

### UTILISATION

1. Ouvrez le projet dans un IDE (ex : Visual Studio Code)

2. Éxecuter le fichier main.py dans une invite de commande. Le fichier va ainsi installer les fichiers de données necessaires

   $ python main.py

3. Ouvrez un navigateur web et "Ctrl + click gauche" sur le lien donné dans l'invite de commande

   http://127.0.0.1:8050/

Au démarage, il a un petit temps d'attente le temps que les fichiers de données .csv soient lu, il est donc normal que le dashboard ne s'affiche pas instentanément.

Vous pouvez maintenant accéder au Dashboard.

4. Utilisation des graphiques :
   - vous pouvez zoomer sur les graphiques et la carte
   - vous pouvez choisir les données à afficher et cacher
   - ## vous pouvez cacher une donnée dans le camembert en cliquant sur sa représentation dans la légende.

## ANALYSE DES DONNÉES

ELEMENT 1 : HISTOGRAMME COMPOSITION DES SPORTS EN FONCTIONS DE L'AGE ET DU SEXE

L'utilisateur choisis : - Le sport dans le premier DROPDOWN - La localisation dans le deuxième DROPDOWN - L'année (Entre 2017 et 2019)

=> On génère un histogramme avec le nombre de licenciés dans un sport dans une région en fonction de l'âge (Homme, Femme pour chaque catégorie d'âge)
=> Générer une animation à travers les années

ELEMENT 2 : CARTE DYNAMIQUE CONCENTRATION SPORTIF

L'utilisateur choisis :

- Le sport (Si aucun sport n'est choisis, on prendra le nombre totale de licenciés sur tout les sports)
- L'information (Le nombre de clubs ou le nombre de licenciés ? (radio))

L'utilisateur peut filtrer : - En fonction de l'age - En fonction du sexe

=> On génère une cartre chaud/froid de la france avec la concentration dans un sport dans chaque région
=> Générer une animation à travers les années

ELEMENT 2 : CARTE DYNAMIQUE LE SPORT LE PLUS POPULAIRE PAR REGION

L'utilisateur choisis : - L'année - La catégorie - La sexe

=> On génère une cartre avec pour chaque région de france le sport le plus populaire

ELEMENT 3 : CAMEMBERT DES ACTIVITÉS

L'utilisateur choisis :

- une commune dans le DROPDOWN
- une année dans le SLIDER

=> on génère un camembert représentant l'ensemble des activités des Fédérations de la commune
On peut cliquer sur la légende pour ne plus afficher une des Fédérations

## DEVELOPER GUIDE

### LE PROJET

Le projet est constitué de 4 dossiers à sa racine :

1. Components : le dossier où les @callback sont effectués et le layout de l'application

2. Dashboard : le dossiers ou chaque élément du dashboard possède un fichier python. Le fichier python possède la fonction permettant de faire l'update de l'élément

3. Data : le dossier data contient les fichiers .csv où sont stockées les données liées aux fédérations de chaques communes en France. Le dossier possède 3 ficher indiquant les données de 2019, 2020 et 2021

4. Guides :

### AJOUTER DU CODE

Pour ajouter du code : exemple de l'ajout d'un nouvel élément au Dashboard

1. créer le fichier python lié à l'élément dans le dossier Dashboard avec sa fonction

2. ajouter les Div nécessaires dans le ficier layouts.py

3. effectuer les @callback necessaires dans le fichier callback.py dans le dossier Components

4. ajouter la fonction pour générer le nouvel élémennt dans le fichier data_processing.py

5. Certains DROPDOWNS étant liés entre eux, apporter des changements à certains peut faire apparaitre des bugs, c'est pourquoi nous conseillons de refresh la page afin d'éviter que cela ce produise.

### AJOUTER DES DONNEES

1. ajouter le downloard necessaire dans le fichier get_data.py afin de pouvoir récupérer les données directement dans le projet en fournissant le lien vers le fichier .csv à ajouter.

Le code ira automatiquement l'ajouter au dossier Data en le téléchargeant

!! vérifier que les nouvelles données possèdent le même modèle que les données déjà présentes !!
