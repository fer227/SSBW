from django.db import models
from mongoengine import Document, fields, StringField, ListField, IntField, EmbeddedDocumentField, EmbeddedDocument

# Create your models here.
class Comentario(EmbeddedDocument):
	autor = StringField(required=True)
	contenido = StringField(required=True)

class Foto(EmbeddedDocument):
	pie = StringField(required=True)
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