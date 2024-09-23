from django.db import models

# Create your models here.
class Autor(models.Model):
     
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)

    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Libro(models.Model):
        
        titulo = models.CharField(max_length=50)
        autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
        fecha_publicacion = models.DateField()
        genero = models.CharField(max_length=50)
        editorial = models.CharField(max_length=50)
        idioma = models.CharField(max_length=50)
        cantidad_paginas = models.IntegerField()
        
        def __str__(self):
            return self.titulo

class Prestamos(models.Model):
        
        libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
        fecha_prestamo = models.DateField()
        fecha_devolucion = models.DateField()
        nombre_persona = models.CharField(max_length=50)
        apellido_persona = models.CharField(max_length=50)
        dni = models.IntegerField()
        email = models.EmailField()
        
        def __str__(self):
            return f'{self.nombre_persona} {self.apellido_persona}'