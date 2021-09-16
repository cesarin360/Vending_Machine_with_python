from django.urls import path
from . import views

app_name="carro"
urlpatterns = [
    path('agregar/<int:producto_id>/', views.add_product, name="agregar"),
    path('eliminar/<int:producto_id>/', views.delete_product, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_product, name="restar"),
    path('limpiar/', views.clear_products, name="limpiar"),
]

