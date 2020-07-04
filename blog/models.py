from django.db import models
from django.conf import settings

class Cancha(models.Model):
    nombre = models.CharField(max_length=50)
    codInt = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    vestuario = models.BooleanField()
    iluminacion = models.BooleanField()
    cespedSint = models.BooleanField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=255)
    empleado = models.CharField(max_length=50, default='')
    fecha_reserva = models.DateField()
    fecha_turno = models.DateTimeField()

    def fechaDisponible(cancha, fechaTurno):
        return Reserva.objects.filter(cancha=cancha,fecha_turno=fechaTurno)