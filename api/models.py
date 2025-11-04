from django.db import models

# Create your models here.
class Galeria(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    foto_url = models.URLField(blank=True)  # imagen como URL
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Obra(models.Model):
    obra = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    tecnica = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(blank=True)  # imagen como URL desde Supabase
    galeria = models.ForeignKey(Galeria, related_name='obras', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.obra} - {self.artista}"