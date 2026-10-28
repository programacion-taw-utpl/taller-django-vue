from django.db import models

# Create your models here.

class Proyecto(models.Model):

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("desarrollo", "En desarrollo"),
        ("finalizado", "Finalizado"),
    ]

    titulo = models.CharField(max_length=150)
    responsable = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo
