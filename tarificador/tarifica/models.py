from django.db import models

# Create your models here.

#class Llamada(models.Model)
#    duracion = models.DateTimeField("Duracion de llamada")
#    num_marcado = models.IntegerField()
#    destino = models.CharField(max_length = 255)
#    costo = models.FloatField()
#    fecha_llamada = models.DateTimeField('Fecha de llamada')
#    num_origen = models.IntegerField()




class Provider(models.Model):
    name = models.CharField(max_length = 255)
    asterisk_id = models.CharField(max_length = 255)
    def __unicode__(self):
        return self.name


class CDR(models.Model):
    total_cost = models.FloatField()
    date = models.DateTimeField()
    total_incoming_calls = models.IntegerField()
    total_outgoing_calls = models.IntegerField()
    total_failed_calls = models.IntegerField()
    def __unicode__(self):
        return self.total_cost


class Destination(models.Model):
    prefix = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    total_cost = models.FloatField()
    #total_duration = 
    total_calls = models.IntegerField()
    def __unicode__(self):
        return self.description


class Plan(models.Model):
    provider = models.ForeignKey(Provider)
    has_free_numbers = models.BooleanField()
    cost_per_month = models.FloatField()
    has_free_calls = models.BooleanField()
    name = models.CharField(max_length = 255)
    def __unicode__(self):
        return self.name




class FreeNumberPlan(models.Model):
    plan = models.ForeignKey(Plan)
    #destination = models.CharField(max_length = 255)
    free_number = models.IntegerField()
    def __unicode__(self):
        return self.free_number


#class FreeCallsPlan(models Model)
#    plan = models.Foreingkey(Plan)
#    destination = models.CharField(max_length = 255)
#    free_number = models.IntegerField()





