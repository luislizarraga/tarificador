from django.db import models

# Create your models here.


#class CDR(models.Model):
 #   total_cost = models.FloatField()
 #   date = models.DateTimeField()
  #  total_incoming_calls = models.IntegerField()
  #  total_outgoing_calls = models.IntegerField()
  #  total_failed_calls = models.IntegerField()
  #  def __unicode__(self):
   #     return self.total_cost


#class Destination(models.Model):
#    prefix = models.CharField(max_length = 255)
#    description = models.CharField(max_length = 255)
#    type_of_destination = models.CharField(max_length = 255)
#    total_cost = models.FloatField()
#    #total_duration = 
#    total_calls = models.IntegerField()
#    def __unicode__(self):
#        return self.description


#class Plan(models.Model):
    #provider = models.ForeignKey(Provider)
#    has_free_numbers = models.BooleanField()
#    cost_per_month = models.FloatField()
#    has_free_calls = models.BooleanField(default = false)
#    name = models.CharField(max_length = 255)
#    def __unicode__(self):
#        return self.name




#class FreeNumberPlan(models.Model):
#    plan = models.ForeignKey(Plan)
    #destination = models.CharField(max_length = 255)
#    free_number = models.IntegerField()
    #def __unicode__(self):
    #    return self.free_number

class PaymentType(models.Model):
    name = models.CharField(max_length = 255)


class DestinationGroup(models.Model):
    name = models.CharField(max_length = 255)
    prefix = models.CharField(max_length = 255)
    matching_number = models.CharField(max_length = 255)


class TariffMode(models.Model):
    name = models.CharField(max_length = 255)
    def __unicode__(self):
        return self.name


class BaseTariff(models.Model):
    cost = models.FloatField()
    mode = models.ForeignKey(TariffMode)
    destination_group = models.ForeignKey(DestinationGroup)


class Bundles(models.Model):
    name = models.CharField(max_length = 255)
    destination_group = models.ForeignKey(DestinationGroup)
    tariff_mode = models.ForeignKey(TariffMode)
    cost = models.FloatField()




class Provider(models.Model):
    asterisk_id = models.CharField(max_length = 255)
    asterisk_name = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    monthly_cost = models.FloatField()
    provider_type = models.CharField(max_length = 50)
    payment_type = models.ForeignKey(PaymentType)
    channels = models.IntegerField()
    base_tariff = models.ForeignKey(BaseTariff)
    bundles = models.ForeignKey(Bundles)
    destination_group = models.ForeignKey(DestinationGroup)
    period_end = models.DateTimeField()




class Extension(models.Model):
    extension_number = models.IntegerField()
    name = models.CharField(max_length = 255)


class UserDailyDetail(models.Model):
    extension = models.ForeignKey(Extension)
    total_calls = models.IntegerField()
    total_minutes = models.FloatField()
    cost = models.FloatField()
    date = models.DateTimeField()


class UserDestinationDetail(models.Model):
    extension = models.ForeignKey(Extension)
    total_calls = models.IntegerField()
    total_minutes = models.FloatField()
    cost = models.FloatField()
    destination_group = models.ForeignKey(DestinationGroup)


class UserDestinationNumberDetail(models.Model):
    extension = models.ForeignKey(Extension)
    total_calls = models.IntegerField()
    total_minutes = models.FloatField()
    cost = models.FloatField()
    prefix = models.CharField(max_length = 255)
    number = models.IntegerField()


class ProviderDailyDetail(models.Model):
    provider = models.ForeignKey(Provider)
    cost = models.FloatField()
    total_calls = models.IntegerField()
    total_minutes = models.FloatField()
    date = models.DateTimeField()


class ProviderDestinationDetail(models.Model):
    provider = models.ForeignKey(Provider)
    cost = models.FloatField()
    total_calls = models.IntegerField()
    total_minutes = models.FloatField()
    destination_group = models.ForeignKey(DestinationGroup)




