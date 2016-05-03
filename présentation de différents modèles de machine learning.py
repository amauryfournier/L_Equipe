
# coding: utf-8

# ## Modèles de machine learning
# 
# ### Amaury Fournier

# In[2]:

from sklearn import datasets
from sklearn.datasets.mldata import fetch_mldata
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import cross_validation
from sklearn.svm import SVC
import numpy as np


# ### Chargement de deux jeux de donées

# In[3]:

iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

print "dataset Iris :"
print "taille du dataset :", iris.data.shape[0]
print "nombre de features :", iris.data.shape[1]
print "nombre de labels :", np.unique(iris.target).size


print("--------------------")
print "dataset breast_cancer :"
print "taille du dataset :", breast_cancer.data.shape[0]
print "nombre de features :", breast_cancer.data.shape[1]
print "nombre de labels :", np.unique(breast_cancer.target).size


# ### Naive Bayes

# In[4]:

kf = cross_validation.KFold(n=iris.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = iris.data[train], iris.data[test], iris.target[train], iris.target[test]
    gnb = GaussianNB()
    y_pred = gnb.fit(Xtrain,ytrain)
    pred = gnb.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset Iris avec le modèle naive Bayes '
print "nombre d'exemples :", iris.data.shape[0]
print "nombre de features :", iris.data.shape[1]
print "performance en cross-validation (5 folds) :"
print tmp_acc 
print "performance moyenne : ", acc


# In[5]:

#avec le dataset breast_cancer

kf = cross_validation.KFold(n=breast_cancer.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = breast_cancer.data[train], breast_cancer.data[test], breast_cancer.target[train], breast_cancer.target[test]
    gnb = GaussianNB()
    y_pred = gnb.fit(Xtrain,ytrain)
    pred = gnb.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset breast_cancer avec le modèle naive Bayes '
#print "nombre d'exemples :", breast_cancer.data.shape[0]
#print "nombre de features :", breast_cancer.data.shape[1]
print "performance en cross-validation (5 folds) :", tmp_acc 
print "performance moyenne : ", acc


# ### Gradient boosting

# In[6]:

kf = cross_validation.KFold(n=iris.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = iris.data[train], iris.data[test], iris.target[train], iris.target[test]
    gboost = GradientBoostingClassifier(n_estimators=200, max_depth=4)
    y_pred = gboost.fit(Xtrain,ytrain)
    pred = gboost.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset Iris avec le modèle Gradient Boosting '
#print "nombre d'exemples :", iris.data.shape[0]
#print "nombre de features :", iris.data.shape[1]
print "performance en cross-validation (5 folds) :", tmp_acc 
print "performance moyenne : ", acc


# In[7]:

#avec le dataset breast_cancer

kf = cross_validation.KFold(n=breast_cancer.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = breast_cancer.data[train], breast_cancer.data[test], breast_cancer.target[train], breast_cancer.target[test]
    gboost = GradientBoostingClassifier(n_estimators=300, max_features=12)
    y_pred = gboost.fit(Xtrain,ytrain)
    pred = gboost.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset breast_cancer avec le modèle Gradient Boosting '
#print "nombre d'exemples :", breast_cancer.data.shape[0]
#print "nombre de features :", breast_cancer.data.shape[1]
print "performance en cross-validation (5 folds) :", tmp_acc 
print "performance moyenne : ", acc


# ### SVM

# In[8]:

kf = cross_validation.KFold(n=iris.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = iris.data[train], iris.data[test], iris.target[train], iris.target[test]
    svm = SVC(kernel='linear', decision_function_shape='ovr')
    y_pred = svm.fit(Xtrain,ytrain)
    pred = svm.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset Iris avec le modèle SVM '
#print "nombre d'exemples :", iris.data.shape[0]
#print "nombre de features :", iris.data.shape[1]
print "performance en cross-validation (5 folds) :", tmp_acc 
print "performance moyenne : ", acc


# In[9]:

#avec le dataset breast_cancer

kf = cross_validation.KFold(n=breast_cancer.data.shape[0], n_folds=5, shuffle=True)
tmp_acc=[]
for train, test in kf:
    Xtrain, Xtest, ytrain, ytest = breast_cancer.data[train], breast_cancer.data[test], breast_cancer.target[train], breast_cancer.target[test]
    svm = SVC(kernel='linear', decision_function_shape="ovo")
    y_pred = svm.fit(Xtrain,ytrain)
    pred = svm.predict(Xtest)
    tmp_acc.append(np.sum(ytest == pred)*1. / Xtest.shape[0])
    
acc = np.mean(tmp_acc)

print 'pour le dataset breast_cancer avec le modèle SVM '
#print "nombre d'exemples :", breast_cancer.data.shape[0]
#print "nombre de features :", breast_cancer.data.shape[1]
print "performance en cross-validation (5 folds) :", tmp_acc 
print "performance moyenne : ", acc


# In[ ]:



