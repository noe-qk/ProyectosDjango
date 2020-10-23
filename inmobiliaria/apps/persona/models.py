from django.db import models

# Create your models here.

#Tabla Personas
class Persona(models.Model):
    cod_persona = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    cuit_persona = models.CharField(max_length=11, blank=True, null=True)
    tipo_persona = models.CharField(max_length=1, blank=True, null=True)
    nombre_persona = models.CharField(max_length=70, blank=True, null=True)
    mail_persona = models.CharField(max_length=50, blank=True, null=True)
    dom_cod_localidad = models.IntegerField(blank=True, null=True)
    dom_cod_calle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'

#Persona tipo Propietario


class PropietarioPropiedad(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    cod_persona = models.IntegerField()
    fecha_alta = models.DateField(blank=True, null=True)
    escritura_propiedad = models.CharField(max_length=2, blank=True, null=True)
    autorizacion_poder = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario_propiedad'
        unique_together = (('cod_propiedad', 'cod_persona'),)


class TelefonoPersona(models.Model):
    cod_persona = models.IntegerField(primary_key=True)
    telefono_persona = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'telefono_persona'
        unique_together = (('cod_persona', 'telefono_persona'),)