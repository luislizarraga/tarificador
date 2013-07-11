from django.contrib import admin
from tarifica.models import Provider, PaymentType

admin.site.register(Provider)
admin.site.register(PaymentType)
