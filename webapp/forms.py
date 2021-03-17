from django import forms
from webapp.models import Covid


class logins(forms.Form):	
	usuario=forms.CharField(max_length=10)
	contrasena=forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)

class FactorRiesgoForm(forms.ModelForm):
    class Meta:
        model = Covid
        #fields='__all__'
        exclude = ['ID','DECESO']            
        labels = {           
                    'ID': 'ID',
                    'SEXO': 'SEXO',
                    'EDAD': 'EDAD',
                    'NEUMONIA': 'NEUMONIA',
                    'DIABETES': 'DIABETES',
                    'EPOC': 'EPOC',
                    'ASMA': 'ASMA',
                    'INMUSUPR': 'INMUSUPR',
                    'HIPERTENSION': 'HIPERTENSION',
                    'CARDIOVASCULAR': 'CARDIOVASCULAR',
                    'OBESIDAD': 'OBESIDAD',
                    'RENAL_CRONICA': 'RENAL_CRONICA',
                    'TABAQUISMO': 'TABAQUISMO',
                    'COVID':'COVID',
                    'OTRA_COM':'OTRA_COM',
                    'DECESO':'DECESO',
                    
        }
        
