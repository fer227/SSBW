from django.db import models
from django import forms
from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from mongoengine import Document, fields, StringField, ListField, IntField, EmbeddedDocumentField, EmbeddedDocument, DictField

# Create your models here.
class Comentario(EmbeddedDocument):
	autor = StringField(required=True)
	contenido = StringField(required=True)

class Foto(EmbeddedDocument):
	pie = StringField(required=False)
	file = StringField(required=True)

class Excursion(Document):
	#nombre = models.CharField(max_length=100)
	#descripcion = models.TextField(max_length=1000)
	#likes = models.IntegerField(default=0)
	nombre = StringField(max_length=120, required=True)
	descripcion = StringField(required=True)
	likes = IntField(default=0)
	file = StringField(max_length=120, required=False)
	visitas = IntField(default=0)
	tags = ListField(StringField(max_length=20))
	duracion = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentario))
	fotos = ListField(EmbeddedDocumentField(Foto))

class ExcursionSerializer(serializers.Serializer):
	nombre = serializers.CharField(max_length=120)
	descripcion = serializers.CharField(max_length=360)
	likes = serializers.IntegerField(default=0)
	id = serializers.UUIDField()
	file = serializers.CharField(max_length=120)

	def create(self, validated_data):
		excursion = Excursion(nombre = validated_data['nombre'], descripcion=validated_data['descripcion']).save()

		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.foto.append(Foto(file=validated_data['foto'], pie=validated_data['pie']))
			else:
				excursion.foto.append(Foto(file=validated_data['foto'], pie=None))
			
		excursion.save()
		return excursion

	def update(self, excursion, validated_data):
		excursion.nombre = validated_data['nombre']
		excursion.descripcion = validated_data['descripcion']

		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.foto.append(Foto(foto=validated_data['foto'], pie=validated_data['pie']))
			else:
				excursion.foto.append(Foto(foto=validated_data['foto'], pie=None))
			
		excursion.save()
		return excursion


class ExcursionForm(forms.Form):
	nombre = forms.CharField(max_length=120)
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":40}))
	foto = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions= ['jpg'])])
	pie = forms.CharField(max_length=80, required=False)