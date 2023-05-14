# from typing_extensions import Required
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class articulo(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField()
    autor = models.CharField(max_length=50)
    referencias = models.TextField(max_length=500)
    fechaPublicacion = models.DateTimeField(default=datetime.now())
    fechaActualizacion = models.DateTimeField()


class ListaproductosCategoria(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'listaproductos_categoria'


class ListaproductosProducto(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(ListaproductosCategoria, models.DO_NOTHING)
    tipo = models.ForeignKey('ListaproductosTipo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listaproductos_producto'


class ListaproductosTipo(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'listaproductos_tipo'


class TiendaComputadora(models.Model):
    descripcion = models.CharField(max_length=500)
    retroiluminado = models.IntegerField()
    color = models.CharField(max_length=250)
    material = models.CharField(max_length=250)
    lectordehuella = models.IntegerField(db_column='lectorDeHuella')  # Field name made lowercase.
    duracionbateria = models.IntegerField(db_column='duracionBateria')  # Field name made lowercase.
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.
    disco = models.ForeignKey('TiendaDisco', models.DO_NOTHING)
    marca = models.ForeignKey('TiendaMarca', models.DO_NOTHING)
    procesador = models.ForeignKey('TiendaProcesador', models.DO_NOTHING)
    ram = models.ForeignKey('TiendaRam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tienda_computadora'


class TiendaDisco(models.Model):
    descripcion = models.CharField(max_length=250)
    tipo = models.CharField(max_length=250)
    velocidad = models.FloatField()
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.
    marca = models.ForeignKey('TiendaMarca', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tienda_disco'


class TiendaMarca(models.Model):
    descripcion = models.CharField(max_length=500)
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tienda_marca'


class TiendaMarcaprocesador(models.Model):
    descripcion = models.CharField(max_length=200)
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tienda_marcaprocesador'


class TiendaProcesador(models.Model):
    descripcion = models.CharField(max_length=250)
    velocidad = models.FloatField()
    generacion = models.IntegerField()
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.
    marcaprocesador = models.ForeignKey(TiendaMarcaprocesador, models.DO_NOTHING, db_column='marcaProcesador_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tienda_procesador'


class TiendaRam(models.Model):
    descripcion = models.CharField(max_length=500)
    velocidad = models.FloatField()
    fechaactualizacion = models.DateTimeField(db_column='fechaActualizacion')  # Field name made lowercase.
    actualizadopor = models.ForeignKey(User, models.DO_NOTHING, db_column='actualizadoPor_id')  # Field name made lowercase.
    marca = models.ForeignKey(TiendaMarca, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tienda_ram'
