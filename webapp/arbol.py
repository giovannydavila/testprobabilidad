from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from webapp.datos import Datos
from webapp.entprue import EntrenamientoPrueba
import pydotplus
#from sklearn.externals.six import StringIO
#from os import system  
import graphviz 
from graphviz import Source
import pydotplus

class ArbolDecisiones:

    def __init__(self):
        self.__xtrain,self.__xtest,self.__ytrain,self.__ytest=EntrenamientoPrueba().entrenamientoPrueba()
        self.d=Datos()
    
    def ejec(self):

        self.arbolDecision()

    def arbol(self):
        return "aqui va el codigo de arbol"

    def arbolDecision(self):
        arbol=DecisionTreeClassifier()
        arbol.fit(self.__xtrain,self.__ytrain)        
        print(arbol.score(self.__xtest,self.__ytest))
        print(arbol.score(self.__xtrain,self.__ytrain))
        y_pred=arbol.predict(self.__xtest)
        print(y_pred)
        #self.graficar(arbol)

    def graficar(self,arbol):
        #dotfile = StringIO()
        #export_graphviz(arbol,out_file="static/img/arbol.dot",class_names=self.d.etiquetas()[1],feature_names=self.d.etiquetas()[0],impurity=False,filled=True)
        #export_graphviz(arbol, out_file=dotfile) 
        #pydotplus.graph_from_dot_data(dotfile.getvalue()).write_png("static/img/arbol.png'")
        dot_data=export_graphviz(arbol,filled=True,rounded=True)
        graph=pydotplus.graph_from_dot_data(dot_data)
        graph.write_png('static/img/arbol.png')    
        #plt.imshow(plt.imread('static/img/arbol.png'))
        #print(self.d.etiquetas()[1])
        