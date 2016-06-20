
# coding: utf-8

# ## Stage données L'équipe  -- TEST FILE
# 
# ### Amaury Fournier

# In[2]:

import pandas as pd
import numpy as np
import random
import re
import matplotlib.pyplot as plt
import pandas as pd
from os import listdir
from os.path import isfile, join,getsize
import datetime
import csv
import pickle
import json
import smtplib
import pandas_profiling
import chardet
#path = "C:\Users\Data Science 5\Desktop\L_equipe"
path = "W:\L_equipe"
pd.set_option('display.max_columns', None)


# In[6]:

#df = pd.read_pickle(path+'\dataframes\s_dataframe_general_xiti_pages_juin2015_partie2.pkl')
df = pd.read_csv(r"V:\Tables_Sas\L_Equipe\Projet_01042016\tables_brutes\Sessions\sessions_xiti-20151215-_Sessions_EQ_20151215.csv", sep=';')
#df_bas = pd.read_pickle(path+"\s_dataframe_general_xiti_clients.pkl")


# In[3]:

df = pd.read_pickle(path+"\dataframes\s_dataframe_temp_session.pkl")


# In[39]:

now = datetime.datetime.now()
now = datetime.datetime(2015,4,15,23,10)
#if now.hour >= 1 and now.hour <5 : print 'yes'
#if now.hour> 14 : print 'maybe'
#if now.hour> 13 : print 'no'
if now.hour < 0 : print "yes"
print now.time()


# ### Session

# In[43]:

name = "s_dataframe_pages_juin2015_partie2.pkl"
reg = re.match((".*_pages_(.*)\.pkl"), name)
print reg.group(1)


# In[ ]:

df.ServiceTitle = df.ServiceTitle.str.normalize("NFKD")
df.ServiceTitle = df.ServiceTitle.str.encode('ASCII','ignore')
df.loc[df.ServiceTitle.str.contains('Coca')]
#print len(df.ServiceTitle.value_counts(dropna=False))
#df.ServiceTitle.value_counts(dropna=False)


# In[ ]:




# In[3]:

#affiche la totalité des colonnes du dataframe
pd.set_option('display.max_columns', None)

#retourne la liste des csv du répertoire Y:\L_Equipe\tablesbrutes\root\namedir
def makelistcsv(namedir, root):
    path = r'Y:\L_Equipe\tablesbrutes' + "\\" + root +"\\"+ namedir 
    if root == "Ventes en ligne":
        onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f)) if f.endswith('.csv') if f.startswith('EQP') if getsize(join(path,f))>0]
    else :
        onlyfiles = [join(path,f) for f in listdir(path) if isfile(join(path, f)) if f.endswith('.csv') if getsize(join(path,f))>0]
    return onlyfiles

#construit le dataframe du csv
def makedataframe(csv):
    if 'Ventes en ligne' in csv :
        df = pd.read_csv(csv, encoding = 'utf-16')
    else :
        df = pd.read_csv(csv, sep=';')
    return df

#retourne la liste privée des doublons de la liste seq 
def makeunique(seq):
    set = {}
    map(set.__setitem__, seq, [])
    return set.keys()

#retourne le dataframe général du repertoire directory
#directory :{client, session, page, compte, commande, souscription}
#/!\ attention à la ram 
#une fois la fonction executée le dataframe est sauvegardée dans le fichier pickle r"W:\L_equipe\s_dataframe_general_root_directory.txt"
#pensez à reset le kernel.
def makegeneraldataframe(directory ):
        if directory == "client" : 
            i=0
        elif directory == "session" : 
            i=1
        elif directory == "page" :
            i=2
        elif directory == "compte" :
            i=3
        elif directory == "commande" :
            i=4
        elif directory == "souscription":
            i=5
        if i < 3 :
            outfile = r'W:\L_equipe\s_dataframe_xiti.txt'
            l_df= pickle.load(open(outfile, "rb"))
            dfs = []
            for j in l_df[i] : 
                dfs.append(makedataframe(j))
            df_g = pd.concat(dfs)
            df_g.to_pickle(r"W:\L_equipe\s_dataframe_general_xiti_"+directory+".pkl")
            #pickle.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+directory+".txt", "wb" ))
            #json.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_xiti_"+directory+".json", "wb" ))
        elif i>= 3 and i<6 :
            outfile = r'W:\L_equipe\s_dataframe_vel.txt'
            l_df= pickle.load(open(outfile, "rb"))
            dfs = []
            for j in l_df[i-3] : 
                dfs.append(makedataframe(j))
            df_g = pd.concat(dfs)
            df_g.to_pickle(r"W:\L_equipe\s_dataframe_general_vel_"+directory+".pkl")
            #pickle.dump(df_g,  open( r"W:\L_equipe\s_dataframe_general_vel_"+directory+".txt", "wb" )) 
            #json.dump(df_g, open( r"W:\L_equipe\s_dataframe_general_vel_"+directory+".json", "wb" ))

        return df_g


# ## A faire tourner

# In[8]:

df_g_page1 =  pd.read_csv(r"Y:\L_equipe\tablesbrutes\Xiti\Pages\pages_xiti-_pages_20150707.csv", sep=';')
df_g_page2 =  pd.read_csv(r"Y:\L_equipe\tablesbrutes\Xiti\Pages\pages_xiti-_pages_20150706.csv", sep=';')


# In[9]:

df_g = pd.concat((df_g_page1,df_g_page2))


# In[11]:

df_g.to_csv(r"W:\L_equipe\test_page.csv")


# In[3]:




# In[6]:

df_prod = pd.read_pickle(r"C:\Users\Data Science 5\Desktop\L_equipe\s_dataframe_general_vel_PROD42.pkl")
df_prod.sort_values(by='ExplicitPrice')


# In[13]:

#df_prod['SubscriptionCreated'] = pd.to_datetime(df_prod['SubscriptionCreated'], format='%d/%m/%Y %H:%M:%S')
df_prod['derniere_visite'] = pd.to_datetime(df_prod['derniere_visite'])


# In[14]:

df_prod.head(6)


# In[6]:

l =[1,2,3,4,5]
l2 = [1,6,9]
l3 = [1,6]
l4 = l2
print cmp(l,l2)
print cmp(l2,l)
print cmp(l2,l3)
print cmp(l2,l4)


# In[ ]:

df = pd.read_csv(r'V:\Tables_Sas\L_Equipe\Projet_01042016\tables_brutes\clients_premium_2015')
clients_premium_2015


# In[2]:

df = pd.read_csv(r'V:\L_Equipe\Projet_01042016\tables_brutes\clients_premium_2015.csv')


# In[3]:

d = df.id_client.unique()


# In[6]:

data = pd.DataFrame(d)


# In[21]:

data.rename(columns={0:'id_client'}, inplace=True)


# In[26]:

data.to_csv(r'V:\L_Equipe\Projet_01042016\tables_brutes\liste_clients_premium_2015.csv', encoding ='utf-8', index=False, index_label=False)


# ### Exercices pour la formation python

# In[64]:

#pseudo-code quicksort(liste)
#si taille de la liste inférieure ou égale à 1 :
#retourner liste
#sinon 
#pivot = un element de la liste 
#généralement on prend le premier ou le dernier elem
#retirer le pivot de la liste
#initialiser deux nouvelles listes (l_plus_grand et l_plus_petit)
#pour tout les elements restant :
#si element <= pivot le mettre dans la liste l_plus_petit
#sinon le mettre dans la liste l_plus_grand
#retourner concaténation(quicksort(l_plus_petit),pivot,l_plus_grand)



def quicksort(l) :
    if len(l) <=1 :
        return l
    else :
        pivot = l[-1]
        l.pop()
        lg=[]
        ll=[]
        for i in l :
            if i <= pivot :
                ll.append(i)
            else :
                lg.append(i)
    return quicksort(ll)+[pivot]+quicksort(lg)

l=[9,4,7,5,3,2,45,6,56,4,545,45,651,3,2,4,2,1]
l1 = quicksort(l)
l2 = (np.random.rand(10)*100).tolist()
l3= quicksort(l2)
print l3
print l1
        


# In[69]:

get_ipython().magic(u'matplotlib inline')

C = np.random.rand(300,200)
plt.figure()
plt.imshow(C)
plt.colorbar()
plt.show()

