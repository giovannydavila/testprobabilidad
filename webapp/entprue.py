from webapp.datos import Datos
from sklearn.model_selection import train_test_split

class EntrenamientoPrueba:

#Conjunto de entrenamiento y conjunto de prueba
    def entrenamientoPrueba(self):
        datos=Datos()
        x_train, x_test, y_train, y_test = train_test_split(
            datos.dataFrame()[0], datos.dataFrame()[1], test_size=0.05, random_state=1)
        
        return [x_train,x_test,y_train,y_test]
