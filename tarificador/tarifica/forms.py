from django import forms
from tarifica import models

class AddProviderInfo(forms.Form):
    #provider = forms.ChoiceField(choices = , label = 'Selecciona Troncal')
    name = forms.CharField(label = 'Nombre')
    monthly_cost = forms.FloatField(label = 'Renta Mensual')
    period_end = forms.DateTimeField(label = 'Fecha de Corte', input_format = '%d/%m')
    #payment_type = forms.ChoiceField(choices = [(e, e.name) for e in PaymentType.objects.all()], label = 'Modalidad de Pago')
    channels = forms.IntegerField(label = 'Canales')


class AddBaseTariffs(forms.Form):
    destination_group = forms.CharField(max_length = 255, label = 'Localidad')
    prefix = forms.CharField(max_length = 255, label = 'Prefijo')
    matching_number = forms.CharField(max_length = 255, label = 'Expresion Regular')
    #tariff_mode = forms.ChoiceField(choices = [(e, e.name) for e in TariffMode.objects.all()], label = 'Modo')
    cost = forms.FloatField(label = 'Costo')


class AddBundles(forms.Form):
    name = forms.CharField(max_length = 255, label = 'Nombre de Paquete')
    #destination_group = forms.ChoiceField(choices = [(e, e.name) for e in DestinationGroup.objects.all()], label = 'Localidad')
    #tariff_mode = forms.ChoiceField(choices = [(e, e.name) for e in TariffMode.objects.all()], label = 'Modo')
    cost = forms.FloatField(label = 'Costo')


