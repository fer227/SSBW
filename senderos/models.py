from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator
from mongoengine import Document, fields, StringField, ListField, IntField, EmbeddedDocumentField, EmbeddedDocument

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
	visitas = IntField(default=0)
	tags = ListField(StringField(max_length=20))
	duracion = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentario))
	fotos = ListField(EmbeddedDocumentField(Foto))

class ExcursionForm(forms.Form):
	nombre = forms.CharField(max_length=120)
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":40}))
	foto = forms.FileField(required=True, validators=[FileExtensionValidator(allowed_extensions= ['jpg'])])
	pie = forms.CharField(max_length=80, required=False)