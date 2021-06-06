from django.shortcuts import render
from .models import Excursion, ExcursionForm, Foto, ExcursionSerializer
from mongoengine.queryset.visitor import Q
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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

def editar(request, id):
	form = ExcursionForm()
	exc = Excursion.objects.get(id=id)
	form = ExcursionForm({'nombre': exc.nombre, 'descripcion': exc.descripcion})
	context = {
		'form': form,
		'exc': exc
	}

	return render(request, 'senderos/editar.html', context)

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

				exc.fotos = [Foto(pie=input_d.get('pie'), file=nombre_archivo)]
				exc.file = nombre_archivo
				exc.save()
				messages.add_message(request, messages.INFO, 'Excursión añadida')
			except OSError as error:
				print('Error al guardar la foto', error)
				messages.add_message(request, messages.ERROR, 'No se pudo añadir la excursión, algo fue mal')

	return redirect('/')

def editarForm(request, id):

	if request.method == 'POST':
		form = ExcursionForm(request.POST, request.FILES)
		if form.is_valid():
			input_d = form.cleaned_data
			files = request.FILES
			exc = Excursion.objects.get(id=id)
			exc.nombre = input_d['nombre']
			exc.descripcion = input_d['descripcion']
			exc.save()

			if len(files) > 0:
				try:
					nombre_archivo = str(exc.id)
					nombre_archivo = nombre_archivo + '.jpg'
					ruta_foto = os.path.join(settings.BASE_DIR, 'static', 'images', nombre_archivo)

					if os.path.exists(ruta_foto):
						os.remove(ruta_foto)

					with open(ruta_foto, 'wb+') as arch:
						for chunk in files['foto'].chunks():
							arch.write(chunk)

					exc.fotos = [Foto(pie=input_d.get('pie'), file=nombre_archivo)]
					exc.save()
					messages.add_message(request, messages.INFO, 'Excursión editada')

				except OSError as error:
					print('Error al guardar la foto', error)
					messages.add_message(request, messages.ERROR, 'La excursión no se pudo editar')

	return redirect('/')

def detalle(request, id):
	exc = Excursion.objects.get(id=id)

	context = {
		'excursion': exc
	}

	return render(request, 'senderos/detalle.html', context)

def cambiarlikes(request, id):
	exc = Excursion.objects.get(id=id)
	subir = request.GET.get('subir')

	if subir == 'true':
		exc.likes += 1
	elif exc.likes != 0:
		exc.likes -= 1

	exc.save()

	return JsonResponse({"likes": exc.likes}, status=200)

def eliminar(request, id):
	Excursion.objects.get(id=id).delete()
	messages.add_message(request, messages.INFO, 'Excursión eliminada')
	return redirect('/')

class Registro(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

class ExcursionView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def get(self, request, id):
		try:
			e = Excursion.objects.get(id=id)
			serializer = ExcursionSerializer(e)
			return Response(serializer.data)
		except:
			raise Http404

	def delete(self, request, id):
		try:
			e = Excursion.objects.get(id=id)
			e.delete()
			serializer = ExcursionSerializer(e)
			return Response(status=status.HTTP_204_NO_CONTENT)
		except:
			raise Http404

	def put(self, request, id):
		try:
			e = Excursion.objects.get(id=id)
			serializer = ExcursionSerializer(e, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		except:
			raise Http404

class ExcursionesView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def get(self, request):
		excursiones = Excursion.objects.all()
		serializer = ExcursionSerializer(excursiones, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ExcursionSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)