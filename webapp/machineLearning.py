from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from webapp.datos import Datos
from webapp.entprue import EntrenamientoPrueba
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus
import pydot
import graphviz
from pydotplus import graph_from_dot_data
from graphviz import Digraph
from sklearn.metrics import roc_curve  
from sklearn.metrics import roc_auc_score  
import pandas as pd

class MachineLearning:
    def __init__(self,request):
        
        self.__datos = request
        print(self.__datos)
        self.__d=Datos()
        self.__xtrain,self.__xtest,self.__ytrain,self.__ytest=EntrenamientoPrueba().entrenamientoPrueba() 

   #Algoritmo Naive Bayes 
    def procesarDatos(self):        
        contexto={  
                    #'ID':self.__datos["result"][0]["ID"],
                    'SEXO':self.__datos["result"][0]["sexo"],
                    'EDAD':self.__datos["result"][0]["edad"],
                    'NEUMONIA':self.__datos["result"][0]["neumonia"],
                    'DIABETES':self.__datos["result"][0]["diabetes"],
                    'EPOC':self.__datos["result"][0]["epoc"],
                    'ASMA':self.__datos["result"][0]["asma"],
                    'INMUSUPR':self.__datos["result"][0]["inmusupr"],
                    'HIPERTENSION':self.__datos["result"][0]["hipertension"],
                    'CARDIOVASCULAR':self.__datos["result"][0]["cardiovascular"],
                    'OBESIDAD':self.__datos["result"][0]["obesidad"],
                    'RENAL_CRONICA':self.__datos["result"][0]["renal_cronica"],
                    'TABAQUISMO':self.__datos["result"][0]["tabaquismo"],
                    'COVID':self.__datos["result"][0]["covid"],
                    'OTRA_COM':self.__datos["result"][0]["otra_com"]
                                        
                }
        x_test=(self.__d.dataFramePdc(contexto))
        return x_test            

    def naiveBayes(self):
        x_test=self.procesarDatos()
        classifier = GaussianNB()
        classifier.fit(self.__xtrain,self.__ytrain)
        try:
            self.matrizConfusion(classifier,1)
            print("se grafico bien")
        except:
            print("error, no se pudo graficar matriz")
        y_pred=classifier.predict(x_test)
        print(y_pred)
        score=classifier.score(self.__xtest,self.__ytest)    
        return {"result":int(y_pred),"score":float(100*round((score),2))}

    def arbolDecisiones(self):
        x_test=self.procesarDatos()
        arbol=DecisionTreeClassifier(max_depth=10)
        arbol.fit(self.__xtrain,self.__ytrain)
        try:            
            self.matrizConfusion(arbol,2)
            self.graficar(arbol,2)
        except:
            print("error, no se pudo graficar arbol")
        y_pred=arbol.predict(x_test)
        score=arbol.score(self.__xtest,self.__ytest)
        return {"result":int(y_pred),"score":float(100*round((score),2))}        

    def graficar(self,arbol,val):     
        export_graphviz(arbol,out_file = 'webapp/static/webapp/img/arbol.dot',rounded=True,special_characters=True,class_names=self.__d.etiquetas()[1],
                        feature_names=self.__d.etiquetas()[0],impurity = True,filled= True)
        
        with     open('webapp/static/webapp/img/arbol.dot')      as f:
            dot_graph=f.read()                     
        graph = pydotplus.graph_from_dot_data(dot_graph)
        graph.write_png('webapp/static/webapp/img/arbolito'+str(val)+'.png')
        f.closed       
        print(arbol.score(self.__xtest,self.__ytest))

#Estandarizacion de Escala 
    def estandarizacion(self,x_train,x_test):
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.transform(x_test)
        return [x_train,x_test]       

#Matriz de Confusion       
    def matrizConfusion(self,objeto,val):
        y_pred=objeto.predict(self.__xtest) 
        self.grafMatrixDif(y_pred,val)
        self.graficas(y_pred,val)

#Gráfica de matriz de Confusión   
    def grafMatrixDif(self,y_pred,val):
        cm = confusion_matrix(self.__ytest, y_pred)
        print(cm)        
        grafica = sns.heatmap(cm,cmap='Pastel2',annot=True,fmt="d")
        print(grafica)
        plt.ylabel('Valores verdaderos')
        plt.xlabel('Prediciones')
        grafica.set(xlabel='Verdaderos',ylabel='Prediciones') 
        plt.savefig('webapp/static/webapp/img/grafico'+str(val)+'.png',dpi=500, facecolor='gray')
        #linea para borrar la figura actual
        #plt.show()
        plt.clf()
    
    def graficas(self, y_pred,val):
        #y_pred=y_pred[:,1]
        auc=roc_auc_score(self.__ytest,y_pred)
        fpr, tpr, thresholds=roc_curve(self.__ytest,y_pred)
        print('AUC: %.2f' % auc)
        self.plot_roc_curve(fpr,tpr,val)

    def plot_roc_curve(self,fpr, tpr,val):  
        plt.plot(fpr, tpr, color='orange', label='ROC')
        plt.plot([1, 1], [1, 1], color='darkblue', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend()
        plt.savefig('webapp/static/webapp/img/curvaRoc'+str(val)+'.png',dpi=500, facecolor='gray')
        #plt.show()
        plt.clf()