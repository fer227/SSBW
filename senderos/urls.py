from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('add', views.add, name='add'),
    path('formExcursion', views.formExcursion, name='formExcursion'),
    path('editarForm/<str:id>', views.editarForm, name='editarForm'),
    path('detalle/<str:id>', views.detalle, name='detalle'),
    path('editar/<str:id>', views.editar, name='editar')
]