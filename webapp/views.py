from django.shortcuts import render, HttpResponse
from webapp.models import Covid
from django.core.paginator import Paginator
from webapp.forms import FactorRiesgoForm
from webapp.machineLearning import MachineLearning
from django.http import JsonResponse,FileResponse,HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    
    return render(request, "webapp/home.html")

def estadistica(request):
    a = Covid.objects.order_by("ID")        
    paginator = Paginator(a, 15) # Show 5 contacts per page.
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  
    rango = get_range(page_obj.number,page_obj.paginator.page_range)
    return render(request, 'webapp/estadistica.html',{"factorRiesgo": page_obj,
        "page_range" : rango,
    })

def get_range(number,page_range):
    size_range = 10    
    frontera_izq = number - (size_range//2)
    frontera_der = number + (size_range//2)
    length = len(page_range)
    if number <= length:
        if length < size_range:
            return page_range
        else:            
            if(frontera_izq < 0):                
                return page_range[:frontera_der + abs(frontera_izq)]

            elif frontera_der > length:                
                return page_range[frontera_izq + (length - frontera_der) :]
                
            elif(frontera_izq >= 0 and frontera_der <= length):
                return page_range[frontera_izq + 1:frontera_der + 1]

    else:
        return False

   

def pronostico(request):
    
    return render(request, "webapp/pronostico.html",{'form':FactorRiesgoForm()})

def contacto(request):
    
    return render(request, "webapp/contacto.html")


@csrf_exempt
def machineLearning(request,x):   
    request.session['datos']=json.loads(request.body)
    machine_Learning = MachineLearning(request.session['datos'])  
    if (x == 1):
        print("Ejecutado el naive")
        return JsonResponse(machine_Learning.naiveBayes(),safe=False)
    elif x == 2:
        print("Ejecutado el arbol")
        return JsonResponse(machine_Learning.arbolDecisiones(),safe=False)





