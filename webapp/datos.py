from django.forms import model_to_dict
from django.http import JsonResponse
from webapp.models import Covid
import pandas as pd

class Datos:
    def __getDatos(self):
        factorRiesgo= Covid.objects.all()
        
        return  factorRiesgo

    def dataFrame(self):
        factorRiesgo=self.__getDatos()
        dataset = { 
                    'ID':[i.ID for i in factorRiesgo], 
                    'SEXO':[i.SEXO for i in factorRiesgo],
                    'EDAD':[i.EDAD for i in factorRiesgo],
                    'NEUMONIA':[i.NEUMONIA for i in factorRiesgo],
                    'DIABETES':[i.DIABETES for i in factorRiesgo],
                    'EPOC':[i.EPOC for i in factorRiesgo],
                    'ASMA':[i.ASMA for i in factorRiesgo],
                    'INMUSUPR':[i.INMUSUPR for i in factorRiesgo],
                    'HIPERTENSION':[i.HIPERTENSION for i in factorRiesgo],
                    'CARDIOVASCULAR':[i.CARDIOVASCULAR for i in factorRiesgo],
                    'OBESIDAD':[i.OBESIDAD for i in factorRiesgo],
                    'RENAL_CRONICA':[i.RENAL_CRONICA for i in factorRiesgo],
                    'TABAQUISMO':[i.TABAQUISMO for i in factorRiesgo],
                    'COVID' :[i.COVID for i in factorRiesgo],
                    'OTRA_COM':[i.OTRA_COM for i in factorRiesgo],
                    'DECESO':[i.DECESO for i in factorRiesgo]}
                                        
        df = pd.DataFrame(dataset)
        x = df.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14]].values
        y = df.iloc[:, 15].values
        #print(dataset.keys())
        return [x,y]

    def dataFramePdc(self,contexto):
        dataset={   
                    #'ID':[contexto['ID']],
                    'SEXO':[contexto['SEXO']],
                    'EDAD':[contexto['EDAD']],
                    'NEUMONIA':[contexto['NEUMONIA']],
                    'DIABETES':[contexto['DIABETES']],
                    'EPOC':[contexto['EPOC']],
                    'ASMA':[contexto['ASMA']],
                    'INMUSUPR':[contexto['INMUSUPR']],
                    'HIPERTENSION':[contexto['HIPERTENSION']],
                    'CARDIOVASCULAR':[contexto['CARDIOVASCULAR']],
                    'OBESIDAD':[contexto['OBESIDAD']],
                    'RENAL_CRONICA':[contexto['RENAL_CRONICA']],
                    'TABAQUISMO':[contexto['TABAQUISMO']],
                    'COVID':[contexto['COVID']],
                    'OTRA_COM':[contexto['OTRA_COM']]
                }

        df=pd.DataFrame(dataset)
        x=df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13]].values
        return x
    
    #Etiquetas
    def etiquetas(self):
        predictors_labels=[ #'ID',
                            'SEXO',
                            'EDAD',
                            'NEUMONIA',
                            'DIABETES',
                            'EPOC',
                            'ASMA',
                            'INMUSUPR',
                            'HIPERTENSION',
                            'CARDIOVASCULAR',
                            'OBESIDAD',
                            'RENAL_CRONICA',
                            'TABAQUISMO',
                            'COVID',
                            'OTRA_COM'
                            
                            ]
        target_labels=['NO','SI']
        return [predictors_labels,target_labels]     


        

