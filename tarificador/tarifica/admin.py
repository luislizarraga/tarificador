from django.contrib import admin
from tarifica.models import Provider, Destination, Plan, FreeNumberPlan

admin.site.register(Provider)
admin.site.register(Destination)
admin.site.register(Plan)
admin.site.register(FreeNumberPlan)