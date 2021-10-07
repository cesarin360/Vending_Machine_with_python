from django.shortcuts import render, redirect
from .models import *
import store.cambio as c

def store(request):
    products= Producto.objects.all()
    return render(request, 'store/store.html', {"pr":products})
def pagination(request):
    products= Producto.objects.all()
    return render(request, 'store/popup.html', {"pr":products})
def checkout(request):
    products= Producto.objects.all()
    return render(request, 'carro/checkout.html', {"pr":products})
def restar_5(request):
    try:
        c.Cambio(request).restar_5()
    except:
        pass
    return redirect('checkout')
def restar_20(request):
    try:
        c.Cambio(request).restar_20()
    except:
        pass
    return redirect('checkout')
def restar_10(request):
    try:
        c.Cambio(request).restar_10()
    except:
        pass
    return redirect('checkout')