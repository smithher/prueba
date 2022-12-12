from django.db import models
from django.contrib.auth.models import User



class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return  self.nombre


class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=100, blank=True)
    requisitos1=models.CharField(max_length=100, blank=True)
    requisitos2=models.CharField(max_length=100, blank=True)
    requisitos3=models.CharField(max_length=100, blank=True)
    numero=models.CharField(max_length=100, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion=models.CharField(max_length=99999, blank=True)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return  self.titulo



