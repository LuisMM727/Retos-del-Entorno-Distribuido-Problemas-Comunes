from django.db import models

class Gasto(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria} - ${self.monto} ({self.fecha})"