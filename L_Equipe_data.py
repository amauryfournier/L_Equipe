
# coding: utf-8

# ## Stage données L'équipe
# 
# ### Amaury Fournier

# ### Infos

# In[ ]:

# Xiti  /!\ sep=';' OK : 
#Clients 569 fichiers OK
#Pages 570 fichiers OK
#Sessions 566 fichiers OK


#Ventes en ligne  /!\ encoding utf-16 OK :
#Commande 89 fichiers OK
#Compte 90 fichiers OK
#Souscription 90 fichiers OK

#PROD42 : 262 fichiers, csv normal


# ### imports

# In[2]:

import pandas as pd
import numpy as np
import random
from os import listdir
from os.path import isfile, join,getsize,isdir
import csv
import cPickle as pickle
import json
import warnings
import time
#import msgpack


# ### fonctions 

# In[21]:

#n'affiche pas les warnings
warnings.filterwarnings('ignore')
#affiche la totalité des colonnes du dataframe
pd.set_option('display.max_columns', None)


#retourne la liste des csv du répertoire Y:\L_Equipe\tablesbrutes\root\namedir 
#root : {'Ventes en ligne','Xiti'}
#namedir : {'Clients', 'Pages', 'Sessions', 'Souscription', 'Commandes', 'Compte', 'PROD42'}
def makelistcsv(namedir, root):
    path = r'Y:\L_Equipe\tablesbrutes' + "\\" + root +"\\"+ namedir 
    if root == "Ventes en ligne":
        if namedir == 'PROD42' : #cas particulier, il faut aller chercher les différents csv qui ne sont pas tous au même endroit
            onlyfiles = []
            path = r'Y:\L_Equipe\tablesbrutes\Ventes en ligne\PROD_VL\PROD'
            onlyfiles.extend([join(path,f) for f in listdir(path) if isfile(join(path, f)) 
                         if f.endswith('.csv') if "SubscriptionsReport" in f if getsize(join(path,f))>0])
            for d in listdir(path) : 
                if d.startswith('20') and not d.startswith('20141209') and not d.startswith('20141212') and not d.startswith('20141217'):
                    path = r'Y:\L_Equipe\tablesbrutes\Ventes en ligne\PROD_VL\PROD'+"\\"+d
                    onlyfiles.extend([join(path,f) for f in listdir(path) if isfile(join(path, f)) 
                         if f.endswith('.csv') if 'SubscriptionsReport' in f if getsize(join(path,f))>0])
                    
        else : #cas Ventes en ligne, not PROD42
            onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f)) 
                         if f.endswith('.csv') if f.startswith('EQP') if getsize(join(path,f))>0]
    else : #cas Xiti
        onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f)) if f.endswith('.csv') if getsize(join(path,f))>0]
    print "liste des csv finie" 
    return onlyfiles

#construit le dataframe du fichier csv
def makedataframe(csv):
    if 'Ventes en ligne' in csv :
        if 'PROD' in csv :
            df = pd.read_csv(csv, encoding = 'utf-8')
        else : #cas Ventes en ligne, not PROD
            df = pd.read_csv(csv, encoding= 'utf-16')
    else : #cas Xiti
        df = pd.read_csv(csv, sep=';', encoding = 'utf-8')
    return df

#retourne la liste privée des doublons de la liste seq 
def makeunique(seq):
    set = {}
    map(set.__setitem__, seq, [])
    return set.keys()

#retourne le dataframe du fichier namedir du directory root
#root : {'Ventes en ligne','Xiti'}
#namedir : {'clients', 'pages', 'sessions', 'souscription', 'commandes', 'compte', 'PROD42'}
#/!\ attention à la RAM
#une fois la fonction executée le dataframe est sauvegardé dans le fichier r"W:\L_equipe\s_dataframe_general_root_directory.pkl"
#pensez à reset le kernel après une exécution de cette fonction pour libérer la RAM.
def makegeneraldataframe(namedir, root):
    if namedir == 'pages' : #cas pages : on ne charge qu'un certain nombre de fichiers pour ne pas exploser la RAM
        liste_page = makelistcsv(namedir, root)
        #liste = liste_page[-38:-8] #pour le dernier mois (juin 2015)
        liste = liste_page[-69:-38] #pour mai 2015
        #liste = liste_page[-99 : -69] #avril 2015
        #liste = liste_page[-130  : -99] #mars 2015
    elif namedir == 'sessions' : #cas sessions :
        liste_session = makelistcsv(namedir, root)
        #liste = liste_session[-30:] #pour le dernier mois (juin 2015)
        #liste = liste_session[-61:-30] #pour mai 2015
        #liste = liste_session[-91:-61]# avril 2015
        liste = liste_session[-122:-91] #mars 2015
        #liste = liste_session[-122:] #mars-juin 2015
    else :
        liste = makelistcsv(namedir,root)
    df_g = pd.concat((makedataframe(f) for f in liste))
    #tentative de découpage du dataframe en deux parties:

    
    if root == "Ventes en ligne" :
        #df_g.to_csv(r"W:\L_equipe\s_dataframe_general_vel_"+namedir+".csv", index=False, encoding='utf-16')
        #df_g.to_json(r"W:\L_equipe\s_dataframe_general_vel_"+namedir+".pkl")
        #msgpack.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_vel_"+namedir+".pkl", "wb" ))
        df_g.to_pickle(r"C:\Users\Data Science 5\Desktop\L_equipe\s_dataframe_general_vel_"+namedir+".pkl")
        #pickle.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_vel_"+namedir+".txt", "wb" ))
        #json.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+directory+".json", "wb" ))
    elif namedir == 'pages'  :
        if (df_g.shape[0])%2 >0 :
            part1 = df_g.shape[0]/2
            part2 = df_g.shape[0]/2 +1
        else : 
            part1 = df_g.shape[0]/2
            part2 = df_g.shape[0]/2
        df_g_p1 = df_g.head(part1)
        df_g_p2 = df_g.tail(part2)
        #return df_g_p1,df_g_p2
        #df_g.to_json(u"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_"+str(len(liste))+".json")
        #msgpack.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_"+str(len(liste))+".pkl", "wb" ))
        #df_g.to_pickle(r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_juin2015_partie1.pkl")
        
        #df_g_p1.to_pickle(r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_mai2015_partie1.pkl")
        df_g_p1.to_pickle(r"C:\Users\Data Science 5\Desktop\L_equipe\s_dataframe_general_xiti_"+namedir+"_mai2015_partie1.pkl")
        
        #df_g_p2.to_pickle(r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_mai2015_partie2.pkl")
        df_g_p2.to_pickle(r"C:\Users\Data Science 5\Desktop\L_equipe\s_dataframe_general_xiti_"+namedir+"_mai2015_partie2.pkl")
        
        #df_g.to_csv(r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+"_avril15.csv",index=False,encoding='utf-16')
        #pickle.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+".txt", "wb" ))
        #json.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+directory+".json", "wb" ))
    else : 
        #msgpack.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+".pkl", "wb" ))
        #df_g.to_json(u"W:\L_equipe\s_dataframe_general_xiti_"+namedir+".json")
        df_g.to_pickle(r"W:\L_equipe\dataframes\s_dataframe_general_xiti_"+namedir+"_mars2015.pkl")
        #df_g.to_csv(r"W:\L_equipe\s_dataframe_general_xiti_"+namedir+".csv", index=False,encoding='utf-16')
    print "pickle pret"

#pour un dataframe donné retourne la liste privée de doublons du champ
#dataframe : {"df_g_client","df_g_page", "df_g_session", "df_g_souscription", "df_g_commande", "df_g_compte", "df_g_prod"}
#champs : voir dictionnaire des données
def makelist(dataframe, champ) : 
    l =[]
    if dataframe in globals() :
        df = eval(dataframe)
        l.extend(df[champ].unique())
    else : 
        print 'il faut créer le dataframe'
    return l



# ### Création des dataframes 

# In[22]:

#une seule exec nécessaire pour créer les pickles
start_time = time.clock()
#makegeneraldataframe("PROD42", "Ventes en ligne")

makegeneraldataframe("sessions", 'Xiti')
#df_g_client = makegeneraldataframe("clients", "Xiti")
#df_g_commande = makegeneraldataframe("commande", "Ventes en ligne")
#df_g_souscription = makegeneraldataframe("souscription",  "Ventes en ligne")
#df_g_prod42 = makegeneraldataframe("PROD42",  "Ventes en ligne")
#df_g_compte = makegeneraldataframe("compte", 'Ventes en ligne')
print time.clock() - start_time, "seconds"


# In[ ]:

#loading pickle
start_time = time.clock()
#df_g_session = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_xiti_sessions_30.pkl") 
#df_g_client = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_xiti_clients.pkl")
#df_g_page = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_xiti_pages_30juin15.pkl")
#df_g_commande = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_vel_commande.pkl")
df_g_commande = pd.read_csv(r"W:\L_equipe\s_dataframe_general_vel_commande.csv", encoding='utf-16')
#df_g_compte = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_vel_compte.pkl")
#df_g_souscription = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_vel_souscription.pkl")
#df_g_prod = pd.read_pickle(r"W:\L_equipe\s_dataframe_general_vel_PROD42.pkl")

#fichiers result de copy /!\ totalement bugman les fichiers sont mal concaténés maybe gérables :
#df_g_client = pd.read_csv(r"W:\L_equipe\all_clients.csv", sep=';')
#df_g_page =  pd.read_csv(r"W:\L_equipe\pages_avril2015_clean.csv")
#df_g_commande = pd.read_csv(r"W:\L_equipe\all_commandes2.csv", encoding = 'utf-16', error_bad_lines=False)
#df_g_compte = pd.read_csv(r"W:\L_equipe\all_comptes.csv", encoding = 'utf-16')
    
#fichiers camille
#df_g_page = makedataframe(u'Y:\L_Equipe\Projet2_072015\Données\Table SAS\PAGEHISTO2.csv')
#df_g_pages = pd.read_csv(u'Y:\L_Equipe\Projet2_072015\Données\Table SAS\PAGEHISTO2.csv', sep=';')
print time.clock() - start_time, "seconds"


# ### creation du datarame pour apprentissage

# In[ ]:

l_client_sub = set(l_liste_xiti[0]) & set(l_liste_vel[0])
l_not_sub = set(l_liste_xiti[0]) - set(l_liste_vel[0])
#random undersampling pour les clients non subs
l_not_sub = random.sample(l_not_sub, 16554)

dftrain = df_g_client.copy()

#on rajoute une colone sub 
dftrain_sub = dftrain.loc[dftrain['id_client'].isin(l_client_sub)]
dftrain_sub_sum = dftrain_sub.groupby(['id_client', 'id_site'], sort=False).sum()
dftrain_sub['sub'] = 1


dftrain_notsub= dftrain.loc[dftrain['id_client'].isin(l_not_sub)]
dftrain_notsub_sum = dftrain_notsub.groupby(['id_client', 'id_site'], sort=False).sum()
dftrain_notsub['sub'] = 0

#dftrain_sub_sum = pd.DataFrame({'visites_sum' : dftrain_sub.groupby(['id_client', 'id_site'])['visites'].sum()}).reset_index()


# In[ ]:

dftrain_tot = pd.concat([dftrain_sub, dftrain_notsub])
dftrain_sum = pd.concat([dftrain_notsub_sum, dftrain_sub_sum])

#dftrain_sum = dftrain_sum.set_index(['id_client'])
#dftrain_sum.rename(columns={'visites': 'visites_sum', 'pages_vues': 'pages_vues_sum'}, inplace=True)
dftraintot = dftrain_tot.join(dftrain_sum, on=['id_client', 'id_site'])


# dataframe contenant les sub et non sub (équilibrés) avec l'id du site le nombre de visites et le nombre de pages vues
dftraintot = dftraintot.drop_duplicates(subset=['id_client','id_site'])
dftraintot.drop(['visites', 'pages_vues'], axis=1, inplace=True)

#len(df[(df['A']>0) & (df['B']>0) & (df['C']>0)])
print 'sub' , len(dftraintot[dftraintot['sub'] == 1])
print 'non sub' , len(dftraintot[dftraintot['sub'] == 0])


# ### Code pour l'audit

# In[ ]:

#dftraintot.sort(columns='id_client' )
#ajout de la colonne durée
#ajout du temps passé par session
#df_g_client.info
#print df_g_commande['fileid'].value_counts(dropna=False)
#print df_g_souscription.SubscriptionCreated.value_counts(dropna=False)
#print df_g_commande.District.value_counts(dropna=False)
#print ('-------------------------------------------------------')
#print (df_g_pages.value_counts(dropna=False) / len(df_g_page))*100
#print (df_g_page.id_site.value_counts(dropna=False) / len(df_g_page))*100
#print df_g_client.id_site.value_counts(dropna=False)
#print ('-------------------------------------------------------')
#print (df_g_client.id_site.value_counts(dropna=False) / len(df_g_client))*100 

#print (df_g_souscription.SubscriptionCreated[1028])
#df_page = df_g_page.drop(df_g_page.index[df_g_page['id_site'] == 'id_site'])
#df_page[df_page['url'] == 'url']
#df_g_client.premiere_visite.count()
df_page.to_csv(r"W:\L_equipe\pages_avril2015_clean.csv")


# In[ ]:

df_g_page


# In[ ]:

# à garder et à mettre en automatique soon ! (penser aussi aux autres csv qui n'ont pas de format datetime propre)
#df_g_prod['SubscriptionCreated'] = pd.to_datetime(df_g_prod['SubscriptionCreated'])
#df_g_prod['SubscriptionLastUpdated'] = pd.to_datetime(df_g_prod['SubscriptionLastUpdated'])
#df_g_prod['ServiceExpiry'] = pd.to_datetime(df_g_prod['ServiceExpiry'])
df_g_pages['date'] = pd.to_datetime(df_g_pages['date'])


# ### Code partie analytics

# In[ ]:

#visiteurs qui ne sont pas sub en avril, mai 2015 et qui ont souscrit en juin 2015
df_g_pages_avril.id_client
df_g_pages_mai
df_g_pages_juin 


# ### Notes à conserver

# In[ ]:

#items à save :
#df Xiti (fichier s_dataframe_xiti) : l_dataframe_xiti = [l_df_client, l_df_page, l_df_session] 
#listes Xiti (fichiers s_liste_xiti): l_liste_xiti = [l_client_unique, l_page_unique, l_session_unique]
#df Vente en ligne (fichier s_dataframe_vel) : l_dataframe_vel = [l_df_sub, l_df_commande, l_df_compte] 
#listes Vente en ligne (fichiers s_liste_vel): l_liste_vel = [l_sub_unique, l_commande_unique] (compte à rajouter s'il le faut)

#----------------------------1er jet test du pickleling OK-----------------------

#l_dataframe = [l_df_sub, l_df_client, l_df_page, l_df_session]
#l_liste = [l_sub_unique, l_client_unique, l_page_unique, l_session_unique]
#
#outfile_df = r'W:\L_equipe\s_dataframe.txt'
#outfile_liste = r'W:\L_equipe\s_liste.txt'
#
#pickle.dump(l_dataframe,  open( r"W:\L_equipe\s_dataframe.txt", "wb" ))
#pickle.dump(l_liste,  open( r"W:\L_equipe\s_liste.txt", "wb" ))

#----------------------------pickle propre OK ----------------------------

l_dataframe_xiti = [l_df_client, l_df_page, l_df_session]
l_liste_xiti = [l_client_unique, l_page_unique, l_session_unique]

outfile_df_xiti = r'W:\L_equipe\s_dataframe_xiti.txt'
outfile_liste_xiti = r'W:\L_equipe\s_liste_xiti.txt'

pickle.dump(l_dataframe_xiti,  open( r"W:\L_equipe\s_dataframe_xiti.txt", "wb" ))
pickle.dump(l_liste_xiti,  open( r"W:\L_equipe\s_liste_xiti.txt", "wb" ))

l_dataframe_vel = [l_df_sub, l_df_commande, l_df_compte] 
l_liste_vel = [l_sub_unique, l_commande_unique]

outfile_df_vel = r'W:\L_equipe\s_dataframe_vel.txt'
outfile_liste_vel = r'W:\L_equipe\s_liste_vel.txt'

pickle.dump(l_dataframe_vel,  open( r"W:\L_equipe\s_dataframe_vel.txt", "wb" ))
pickle.dump(l_liste_vel,  open( r"W:\L_equipe\s_liste_vel.txt", "wb" ))

