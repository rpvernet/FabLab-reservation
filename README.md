# Fab Lab reservation system

## Project description
It all started with a need. We needed a reservation system for the Fab lab at my work. We were using a generic reservation system, but it was only reserving the equipment. We detain more than ten pieces of equipment, but only two employees. We never found a reservation system that allowed us to manage the equipment and the employees’ availability. 
The system I built allows the creation of accounts and reservation of equipment. It was built to be configurable. It uses a point system for the employees’ availability depending on a schedule. It’s possible to create different types of reservation that have different values on the point system. Each reservation type can be attributed to a machine. 
There is also a badge system. Some kinds of reservations are only available if the user has a certification for the machine.
Please note that the project was never used. 
 
## Technologies
Like a lot of people, my first programming experience was with Python. The best framework with Python is Django, so it uses Django. CSS was handled with Sass. For the rest, it’s standard. It’s to be noted that it’s pure Django. It’s not a Django REST project. 
The database is PostgresSQL, because it’s the database of predilection for Django. It gives the most features to Django.
The deploy method is Docker.
 
## What I would have done differently
The project started for a very precise need, so it has a lot of non standard features for a reservation system. We are getting farther from the YAGNI principle. Maintaining all the features in a production context could become difficult.
 
## If I have more time
The project is getting old, so I would update the dependencies. Also, I would produce documentation on how to install the project on a Linux server. 

-----------------------------------------------------------------------------------------------------------------------------------------------------
# Fab Lab reservation system - français

## Description du projet
Cela a commencé avec un besoin fonctionnel : un système de réservation pour le Fab lab à mon travail. Nous utilisions un système de réservation générique, mais il ne gérait que l’équipement. Nous avons plus d’une dizaine de pièces d’équipement, mais seulement deux employés sur le plancher. Nous ne trouvions pas de système de réservation qui permettait de gérer à la fois la disponibilité des équipements et des employés. 
Le système que j’ai bâti permet de créer un compte et de réserver les équipements. Il a été conçu pour être le plus paramétrable possible. Il possède un système de points de disponibilité par employé selon un horaire, cela est configurable. Il est possible de créer plusieurs types de réservations et de leur attribuer une valeur. Nous pouvons choisir le type de réservation par machine. Il y a aussi un système de badge : les types de réservation plus avancés sont seulement disponibles si l’usager est certifié sur la machine. 
Il est à noter que le système n’a jamais été utilisé. 

## Technologies
Comme pour plusieurs personnes, mon premier rapport plus concret avec la programmation a été avec Python. Le meilleur framework pour Python est Django. Le CSS a été géré avec Sass. Pour le reste, c’est assez standard. Il est à noter que c’est du Django pur. Il n’est pas utilisé comme un REST API ou autre. 
La base de données est PostgreSQL, car il s’agit de la base de données de prédilection pour Django. C’est celle qui donne le plus de fonctionnalités à Django.
Le déploiement se fait par Docker.

## Ce que je ferais différemment
Le projet est parti d’un besoin très précis, donc il possède plusieurs fonctionnalités non-standards pour un système de réservations. On s’éloigne probablement du principe YAGNI. Le maintien de l’ensemble de ces fonctionnalités dans un contexte de production pourrait devenir complexe, donc il faudrait déterminer lesquels sont vraiment nécessaires.

## Si j’avais plus de temps
Le projet date un peu, donc je mettrais à jour les dépendances. Je produirais aussi une documentation pour l’installation du projet sur un serveur Linux. 


