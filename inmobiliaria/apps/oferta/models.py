from django.db import models

# Create your models here.
class Oferta(models.Model):
    cod_oferta = models.IntegerField(primary_key=True)
    permite_cancelacion = models.CharField(max_length=2, blank=True, null=True)
    fecha_inicio_oferta = models.DateField(blank=True, null=True)
    fecha_fin_oferta = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oferta'



#Ofertas de los alquileres
class OfertaAlquiler(models.Model):
    cod_oferta = models.IntegerField(primary_key=True)
    cod_propiedad = models.IntegerField()
    fec_solicitud = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oferta_alquiler'
        unique_together = (('cod_oferta', 'cod_propiedad'),)


#Propiedad Oferta -- 
class PropiedadOferta(models.Model):
    cod_oferta = models.IntegerField()
    cod_propiedad = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'propiedad_oferta'
        unique_together = (('cod_propiedad', 'cod_oferta'),)
