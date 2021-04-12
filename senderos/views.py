from django.shortcuts import render
from .models import Excursion
from mongoengine.queryset.visitor import Q

# Create your views here.
def index(request):
	excursiones = Excursion.objects.all()
	return render(request, 'senderos/index.html', {'excursiones': excursiones})

def buscar(request):
	busqueda = request.POST.get('busqueda', '')

	context = {
		'excursiones' : Excursion.objects(Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)),
		'buscado' : True
	}

	return render(request, 'senderos/index.html', context)