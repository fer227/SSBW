from django.shortcuts import render
from .models import Excursion

# Create your views here.
def index(request):
	excursiones = Excursion.objects.all()
	return render(request, 'senderos/index.html', {'excursiones': excursiones})

def buscar(request):
	busqueda = request.POST.get('busqueda', '')

	context = {
		'buscado' : busqueda,
	}

	return render(request, 'senderos/index.html', context)