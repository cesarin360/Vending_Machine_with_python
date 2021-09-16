from django.shortcuts import render, redirect
from .carro import Carro
from store.models import Producto

def add_product(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.add(producto=producto)
    return redirect("store")
def delete_product(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.delete(producto=producto)
    return redirect("store")
def restar_product(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_pr(producto=producto)
    return redirect("store")
def clear_products(request):
    carro=Carro(request)
    carro.clear_car()
    return redirect("store")
