# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


#Indica el estado de la propiedad 'Construccion' 'Ampliacion' 'Remodelacion'
class Estado(models.Model):
    cod_estado = models.IntegerField(primary_key=True)
    descrip_estado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


#Tipo de Propiedad Casa
class PropCasa(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    patio = models.CharField(max_length=2, blank=True, null=True)
    pileta = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prop_casa'

#Tipo de Propiedad Departamento
class PropDpto(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    frente = models.CharField(max_length=2, blank=True, null=True)
    contrafrente = models.CharField(max_length=2, blank=True, null=True)
    espacios_comunes = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prop_dpto'


#Tipo de Propiedad Habitacion
class PropHabitacion(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    banio_individual = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prop_habitacion'


class Propiedad(models.Model):
    cod_propiedad = models.IntegerField(primary_key=True)
    tipo_propiedad = models.IntegerField(blank=True, null=True)
    mtrs2_cubiertos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    mtrs2_semicubiertos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    cant_banios = models.IntegerField(blank=True, null=True)
    cant_ambientes = models.IntegerField(blank=True, null=True)
    permite_cancelacion = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propiedad'





class TelefonoPersona(models.Model):
    cod_persona = models.IntegerField(primary_key=True)
    telefono_persona = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'telefono_persona'
        unique_together = (('cod_persona', 'telefono_persona'),)


class TipoPropiedad(models.Model):
    tipo_propiedad = models.IntegerField(primary_key=True)
    descrip_tipo_propiedad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_propiedad'


class Zona(models.Model):
    cod_zona = models.IntegerField(primary_key=True)
    descrip_zona = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona'
