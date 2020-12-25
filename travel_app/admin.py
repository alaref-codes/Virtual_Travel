from django.contrib import admin

from travel_app.models import Country,Language,bestPlace,Trafood

# Register your models here.

admin.site.register(Country)
admin.site.register(bestPlace)
admin.site.register(Trafood)
admin.site.register(Language)
