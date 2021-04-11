# populate.py
from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField
from datetime import datetime

connect('senderos_db', host='mongo')

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

comentarios = [
	{
		'contenido': 'Primer comentario',
		'autor': 'Yo'
	},
    {
		'contenido': 'Segundo comentario',
		'autor': 'Otro'
	}
]

fotos = [
	{
		'pie': 'primera foto',
		'file': 'foto1.jpg'
	},
    {
		'pie': 'segunda foto',
		'file': 'foto2.jpg'
	}
]

excursion = Excursion(nombre="Primera excursión", descripcion="Una descripción", likes=1, 
                      tags=['fácil'], comentarios=comentarios, fotos=fotos)
excursion.save() # Para escribir en la BD

...

for excursion in Excursion.objects():
	print(excursion.nombre)