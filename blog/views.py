from django.shortcuts import get_object_or_404, redirect, render
from .models import Cancha, Reserva
from django.http import JsonResponse
from datetime import time
from django.utils import timezone
from django.contrib import messages

def lista_canchas(request):
    canchas = Cancha.objects.all()
    return render(
        request,
        'listadoCanchas.html',
        {'canchas': canchas}
    )

def filtrarCesped(request):
    canchas = Cancha.objects.filter(cespedSint=True)
    return render(
        request,
        'listadoCanchas.html',
        {'canchas': canchas}
    )

def filtrarVestuario(request):
    canchas = Cancha.objects.filter(vestuario=True)
    return render(
        request,
        'listadoCanchas.html',
        {'canchas': canchas}
    )

def filtrarIlu(request):
    canchas = Cancha.objects.filter(iluminacion=True)
    return render(
        request,
        'listadoCanchas.html',
        {'canchas': canchas}
    )

def detalle_cancha(request, id):
    cancha = get_object_or_404(Cancha, pk=id)
    reservas = Reserva.objects.filter(cancha=cancha.pk)
    allCanchas = Cancha.objects.all()
    return render(
        request,
        'detalleCancha.html',
        {'cancha': cancha, 'reservas': reservas, 'allCanchas': allCanchas}
    )

def eliminarReserva(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    return redirect('detalleCancha', reserva.cancha.pk)

def nuevaReserva(request):
    reserva = Reserva()
    allCanchas = Cancha.objects.all()
    if request.method == 'POST':
        cancha = Cancha.objects.get(pk=request.POST['cancha'])
        reserva.cancha = cancha
        reserva.cliente = request.POST['cliente']
        reserva.empleado = request.POST['empleado']
        reserva.fecha_reserva = timezone.now()
        fechaTurno = request.POST['fechaTurno']
        if not Reserva.fechaDisponible(cancha, fechaTurno):
            reserva.fecha_turno = fechaTurno
            reserva.save()
            return JsonResponse({'ok': 'ok'})
            #return redirect('listado')
        else:
            return JsonResponse({'ok': 'fecha'})
        #     return render(
        #     request,
        #     'nuevaReserva.html',
        #     {'canchas': allCanchas, 'reserva': reserva}
        # )
    else:
        return render(
            request,
            'nuevaReserva.html',
            {'canchas': allCanchas, 'reserva': reserva, 'editar': False}
        )

def editarReserva(request, id):
    reserva = Reserva.objects.get(pk=id)
    if request.method == 'POST':
        cancha = Cancha.objects.get(pk=request.POST['cancha'])
        reserva.cancha = cancha
        reserva.cliente = request.POST['cliente']
        reserva.empleado = request.POST['empleado']
        reserva.fecha_reserva = timezone.now()
        reserva.fecha_turno = request.POST['fechaTurno']
        reserva.save()
        return redirect('listado')
    else:
        allCanchas = Cancha.objects.all()
        return render(
            request,
            'editarReserva.html',
            {'canchas': allCanchas, 'reserva': reserva}
        )