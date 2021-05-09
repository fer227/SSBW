from django.urls import path
from . import views
from .views import Registro

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('add', views.add, name='add'),
    path('formExcursion', views.formExcursion, name='formExcursion'),
    path('editarForm/<str:id>', views.editarForm, name='editarForm'),
    path('detalle/<str:id>', views.detalle, name='detalle'),
    path('editar/<str:id>', views.editar, name='editar'),
    path('eliminar/<str:id>', views.eliminar, name='eliminar'),
    path('registro/', Registro.as_view(), name='registro'),
    path('api/excursion/<id>', views.ExcursionView.as_view(), name="excursion"),
    path('api/excursiones', views.ExcursionesView.as_view(), name="excursiones"),
    path('cambiarlikes/<str:id>/', views.cambiarlikes, name="cambiarlikes")
]