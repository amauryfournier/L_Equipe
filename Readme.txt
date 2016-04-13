Repo admin : Amaury Fournier

Ce README sert non seulement de pr�sentation du repo mais aussi de bloc-note pour le rapport final.

Etude portant sur le comportement des visiteurs simples des diff�rents sites de l'Equipe sur la p�riode mars-juin 2015.
Un client est consid�r� comme visiteur simple s'il n'a jamais souscrit � un abonnement.
Le but de l'�tude est de trouver des clients qui ont une forte probabilit� de souscrire � un abonnement de l'Equipe payant.


/!\ chaque soir lancer un truc long � tourner pour ne pas avoir � le faire pendant la journ�e.


--------------------------------------------------------
Les clients que l'on s�lectionne ont fait au moins une visite entre mars et mai 2015 et au moins une en juin 2015

Mars - Avril - Mai : On r�cup�re les clients (abonn�s et simples visiteurs) ayant fait une visite pendant cette p�riode d'observation.
On y trouve un comportement de navigation de ces 3 derniers mois (r�cup�r� dans les fichiers pages et sessions)
ainsi que les diff�rentes infos r�cup�r�es sur le client (autres fichiers). 

Juin : P�riode de pr�diction de souscription qui contient un comportement de navigation 
sur le mois de juin (encore les fichiers pages et sessions) ainsi qu'un label indicant si le client est abonn� ou simple visiteur.

Pour ajouter un prefixe au colonnes au dataframe de juin : 
df.rename(columns = lambda x : 'juin_' + x)

recence_de_visite  = 30 : derniere_visite = 01/6/2015
recence_de_visite = 1 : derniere_visite = 30/6/2015
---------------------------------------------------------

Garder le fichier sur disque r�seau propre et � jour!

Choix � faire sur les fichiers Pages (en une ou deux parties selon les diff�rents r�sults)
Pickle provoque des erreurs pour la s�rialisation de dataframes trop volumineux

Penser � mettre les ipython notebooks en sauvegarde sur le disque serveur ou sur dropbox. OK

#Pour chaque portions du pie de la dur�e de souscription (les portions les plus importantes) :
#Faire le graphe de la distribution des prix mensuels des abonn�s, ou alors faire un graphe regrouppant toutes les infos mais propre.
#Par exemple un group by sur le temps de souscription puis des bares pour les diff�rents prix. (un peu comme le graphe des abonn�s par mois)

faire le clean des subs en ne gardant que ceux qui correspondent � l'�tude. (via tiers payant et �quipe payant)
attention � la p�riode on ne veut que des abonn�s qui se sont abonn�s en juin et qui �taient simple visiteurs avant.
faire une visualisation du comportement des abonn�s avant souscription maybe ? 
(regroupement avec autres dataframes peut etre le faire apr�s fusion).

puis faire le clean propre pour les autres tables.

d�s que clients OK faire la mise � jour du fichier excel 

regarder l'audit pour les variables (feuilles variables et apper�u des tables)

r�fl�chir aux fichiers pages pas forc�ment compliqu�,
mais il y aura des regroupements � faires une fois les diff�rentes parties fusionn�es.
	-bien d�finir le group by pour pages (attention � l'unicit� du regroupement)
	-bien d�finir le calcul fait sur le regroupement pour chaque variables

r�fl�chir aussi � la fusion des sessions et pages sur les 3 mois.
--------------------------------------------------------
Format � respecter imp�rativement 
--------------------------------------------------------

-fichiers issus de la concat�nation des CSV : s_dataframe_general_repo_name.ext
-datasets utilis�s pour les �tudes annexes : s_dataframe_etude_name.ext
-datasets en cours de clean/partiellement clean : s_dataframe_temp_name.ext
-datasets clean pr�ts � la concat�nation finale : s_dataframe_final_name.ext

Pas d'autres noms autoris�s 

liste � normaliser (si le moindre doute recommencer le process) :
compl�ter

--------------------------------------------------------
It's complicated (dans cette section les diff�rentes difficult�s, incoh�rences, ab�rations ...)
--------------------------------------------------------
Format :
Les fichiers viennent de sources diff�rentes et ne sont pas forc�ment s�rialis�s sous le m�me format.
Pour les fichiers Xiti : csv  ... 

Variables :
Sub  : 
-ServiceTitle et ServiceDescription n'ont aucune rigueur sur le format -> obliger de tout reformater � la main
-Abo Premium ! probl�me
-Pas les m�me sub dans les tables commandes et PROD42
-It�ret de AccountId???


Commandes :
AccountID -> Useless
OrderID ->Useless
MPPGiftCode semble etre l'id de la souscription (c'est gr�ce � cette variable que l'on peut groupper par souscription)
-------------------------------------------------------
TODO
-------------------------------------------------------
transf�rer les dataframes finaux sur disque externe ou autre moyen de sauvegarder le travail.

r�fl�chir au fait d'utiliser spyder pour lancer des taches planif�es pendant toute la nuit (avec chron ou la lib d'antoine)

mise � jour des evenements majeurs sur la p�riode consid�r�e (voir le fichier excel audit_et_notes_utiles)

mise � jour � pr�voir pour l'audit de l'Equipe

mise en place des mod�les sous python.

ppt formation python : archi en cours de validation 

ppt mod�les machine learning : en cours, il faut le retravailler, il doit �tre abordable pour des non-datascientists

r�colter diff�rentes infos sur les archis big data pour la formation
-Google cloud semble friendly user
-AWS (copie de la r�ponse d'antoine S) :
Les avantages je sais pas trop. Mais AWS offre plein d'outils, dont la bonne moiti� sont orient�s Big Data. 
Tu peux �galement y h�berger d'autres outils comme R studio ou ipython, avec des forfaits sur la ram/puissance 
de calcul que tu veux allouer (genre pour R c'est 30centimes/jour pour 30Go de m�moire vive).
Apr�s les outils en d�tail je connais rien sauf leur base de donn�e Redshift qui est une BD orient� "colonne" (en gros �a veut
dire opti pour les select : affichage, datamining, etc... Mais qui doit �tre plus long pour l'insertion ou un truc comme �a).
Tout ce que je sais c'est que Decathlon a fait le choix de AWS contre microsoft Azur (malgr� que tout soit microsoft chez eux) 
pour des raisons de budget avantageux.