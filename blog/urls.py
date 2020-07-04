from .views import lista_canchas, detalle_cancha, eliminarReserva, nuevaReserva, filtrarIlu, editarReserva, filtrarCesped, filtrarVestuario
from django.urls import path

urlpatterns = [
    path('', lista_canchas, name='listado'),
    path('detalle/<int:id>', detalle_cancha, name='detalleCancha'),
    path('eliminarReserva/<int:id>', eliminarReserva, name='eliminarReserva'),
    path('nuevaReserva', nuevaReserva, name='nuevaReserva'),
    path('editarReserva/<int:id>', editarReserva, name='editarReserva'),
    path('filtrarCesped', filtrarCesped, name='filtrarCesped'),
    path('filtrarVestuario', filtrarVestuario, name='filtrarVestuario'),
    path('filtrarIlu', filtrarIlu, name='filtrarIlu'),
]