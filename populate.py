# populate.py
from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField
from datetime import datetime

connect('senderos', host='mongo')

class Comentarios(EmbeddedDocument):
	contenido = StringField(required=True)
	autor     = StringField(max_length=120, required=True)
	fecha     = DateTimeField(default=datetime.now())

class Excursion(Document):
	nombre      = StringField(max_length=120, required=True)
	descripcion = StringField(required=True)
	likes       = IntField(default=0)
	visitas     = IntField(default=0)
	tags        = ListField(StringField(max_length=20))
	duracion    = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentarios))
	fotos	  = ListField()

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