from django.shortcuts import render
from .models import Excursion, ExcursionForm, Foto
from mongoengine.queryset.visitor import Q
from django.conf import settings
from django.shortcuts import redirect
import os

# Create your views here.
def index(request):
	excursiones = Excursion.objects.all()[:4]
	return render(request, 'senderos/index.html', {'excursiones': excursiones})

def buscar(request):
	busqueda = request.POST.get('busqueda', '')

	context = {
		'excursiones' : Excursion.objects(Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)),
		'buscado' : True
	}

	return render(request, 'senderos/index.html', context)

def add(request):
	form = ExcursionForm()

	context = {
		'form': form
	}

	return render(request, 'senderos/add.html', context)

def formExcursion(request):

	if request.method == 'POST':
		form = ExcursionForm(request.POST, request.FILES)
		if form.is_valid():
			input_d = form.cleaned_data
			files = request.FILES
			exc = Excursion(nombre=input_d['nombre'], descripcion=input_d['descripcion']).save()
			try:
				nombre_archivo = str(exc.id)
				nombre_archivo = nombre_archivo + '.jpg'
				ruta_foto = os.path.join(settings.BASE_DIR, 'static', 'images', nombre_archivo)
				with open(ruta_foto, 'wb+') as arch:
					for chunk in files['foto'].chunks():
						arch.write(chunk)
				exc.foto = [Foto(pie=input_d.get('pie'), file=nombre_archivo)]
				exc.save()
			except OSError as error:
				print('Error al guardar la foto', error)

	return redirect('/')