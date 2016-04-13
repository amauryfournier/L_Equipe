Repo admin : Amaury Fournier

Ce README sert non seulement de présentation du repo mais aussi de bloc-note pour le rapport final.

Etude portant sur le comportement des visiteurs simples des différents sites de l'Equipe sur la période mars-juin 2015.
Un client est considéré comme visiteur simple s'il n'a jamais souscrit à un abonnement.
Le but de l'étude est de trouver des clients qui ont une forte probabilité de souscrire à un abonnement de l'Equipe payant.


/!\ chaque soir lancer un truc long à tourner pour ne pas avoir à le faire pendant la journée.


--------------------------------------------------------
Les clients que l'on sélectionne ont fait au moins une visite entre mars et mai 2015 et au moins une en juin 2015

Mars - Avril - Mai : On récupère les clients (abonnés et simples visiteurs) ayant fait une visite pendant cette période d'observation.
On y trouve un comportement de navigation de ces 3 derniers mois (récupéré dans les fichiers pages et sessions)
ainsi que les différentes infos récupérées sur le client (autres fichiers). 

Juin : Période de prédiction de souscription qui contient un comportement de navigation 
sur le mois de juin (encore les fichiers pages et sessions) ainsi qu'un label indicant si le client est abonné ou simple visiteur.

Pour ajouter un prefixe au colonnes au dataframe de juin : 
df.rename(columns = lambda x : 'juin_' + x)

recence_de_visite  = 30 : derniere_visite = 01/6/2015
recence_de_visite = 1 : derniere_visite = 30/6/2015
---------------------------------------------------------

Garder le fichier sur disque réseau propre et à jour!

Choix à faire sur les fichiers Pages (en une ou deux parties selon les différents résults)
Pickle provoque des erreurs pour la sérialisation de dataframes trop volumineux

Penser à mettre les ipython notebooks en sauvegarde sur le disque serveur ou sur dropbox. OK

#Pour chaque portions du pie de la durée de souscription (les portions les plus importantes) :
#Faire le graphe de la distribution des prix mensuels des abonnés, ou alors faire un graphe regrouppant toutes les infos mais propre.
#Par exemple un group by sur le temps de souscription puis des bares pour les différents prix. (un peu comme le graphe des abonnés par mois)

faire le clean des subs en ne gardant que ceux qui correspondent à l'étude. (via tiers payant et équipe payant)
attention à la période on ne veut que des abonnés qui se sont abonnés en juin et qui étaient simple visiteurs avant.
faire une visualisation du comportement des abonnés avant souscription maybe ? 
(regroupement avec autres dataframes peut etre le faire après fusion).

puis faire le clean propre pour les autres tables.

dès que clients OK faire la mise à jour du fichier excel 

regarder l'audit pour les variables (feuilles variables et apperçu des tables)

réfléchir aux fichiers pages pas forcément compliqué,
mais il y aura des regroupements à faires une fois les différentes parties fusionnées.
	-bien définir le group by pour pages (attention à l'unicité du regroupement)
	-bien définir le calcul fait sur le regroupement pour chaque variables

réfléchir aussi à la fusion des sessions et pages sur les 3 mois.
--------------------------------------------------------
Format à respecter impérativement 
--------------------------------------------------------

-fichiers issus de la concaténation des CSV : s_dataframe_general_repo_name.ext
-datasets utilisés pour les études annexes : s_dataframe_etude_name.ext
-datasets en cours de clean/partiellement clean : s_dataframe_temp_name.ext
-datasets clean prêts à la concaténation finale : s_dataframe_final_name.ext

Pas d'autres noms autorisés 

liste à normaliser (si le moindre doute recommencer le process) :
compléter

--------------------------------------------------------
It's complicated (dans cette section les différentes difficultés, incohérences, abérations ...)
--------------------------------------------------------
Format :
Les fichiers viennent de sources différentes et ne sont pas forcément sérialisés sous le même format.
Pour les fichiers Xiti : csv  ... 

Variables :
Sub  : 
-ServiceTitle et ServiceDescription n'ont aucune rigueur sur le format -> obliger de tout reformater à la main
-Abo Premium ! problème
-Pas les même sub dans les tables commandes et PROD42
-Itêret de AccountId???


Commandes :
AccountID -> Useless
OrderID ->Useless
MPPGiftCode semble etre l'id de la souscription (c'est grâce à cette variable que l'on peut groupper par souscription)
-------------------------------------------------------
TODO
-------------------------------------------------------
transférer les dataframes finaux sur disque externe ou autre moyen de sauvegarder le travail.

réfléchir au fait d'utiliser spyder pour lancer des taches planifées pendant toute la nuit (avec chron ou la lib d'antoine)

mise à jour des evenements majeurs sur la période considérée (voir le fichier excel audit_et_notes_utiles)

mise à jour à prévoir pour l'audit de l'Equipe

mise en place des modèles sous python.

ppt formation python : archi en cours de validation 

ppt modèles machine learning : en cours, il faut le retravailler, il doit être abordable pour des non-datascientists

récolter différentes infos sur les archis big data pour la formation
-Google cloud semble friendly user
-AWS (copie de la réponse d'antoine S) :
Les avantages je sais pas trop. Mais AWS offre plein d'outils, dont la bonne moitié sont orientés Big Data. 
Tu peux également y héberger d'autres outils comme R studio ou ipython, avec des forfaits sur la ram/puissance 
de calcul que tu veux allouer (genre pour R c'est 30centimes/jour pour 30Go de mémoire vive).
Après les outils en détail je connais rien sauf leur base de donnée Redshift qui est une BD orienté "colonne" (en gros ça veut
dire opti pour les select : affichage, datamining, etc... Mais qui doit être plus long pour l'insertion ou un truc comme ça).
Tout ce que je sais c'est que Decathlon a fait le choix de AWS contre microsoft Azur (malgré que tout soit microsoft chez eux) 
pour des raisons de budget avantageux.