from django.shortcuts import get_object_or_404, render

from personas.models import Persona

# Create your views here.

def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})