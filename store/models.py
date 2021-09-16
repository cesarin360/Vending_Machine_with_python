from django.db import models

class CatProduct(models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="catProduct"
        verbose_name_plural="catsProduct"
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CatProduct, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="store", null=True, blank=True)
    code = models.CharField(max_length=4)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"
