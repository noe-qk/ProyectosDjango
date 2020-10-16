from django.db import models

# Create your models here.

class AlquilerPropiedad(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    cod_persona = models.IntegerField()
    importe_alquiler = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fec_alquiler_desde = models.DateField(blank=True, null=True)
    fec_alquiler_hasta = models.DateField(blank=True, null=True)
    cant_personas = models.IntegerField(blank=True, null=True)
    importe_senia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alquiler_propiedad'
        unique_together = (('cod_propiedad', 'cod_persona'),)



#Indica si una propiedad esta alquilada o disponible
#Consutar Modelo - Propiedad tambien?
class EstadoPropiedad(models.Model):
    cod_propiedad = models.IntegerField()
    cod_estado = models.IntegerField(primary_key=True)
    fecha_estado_desde = models.DateField(blank=True, null=True)
    fecha_estado_hasta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_propiedad'
        unique_together = (('cod_estado', 'cod_propiedad'),)

