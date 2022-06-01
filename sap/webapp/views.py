from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    nro_personas_var = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'nro_personas': nro_personas_var, 'personas': personas})
