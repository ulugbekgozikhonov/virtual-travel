from django.contrib import admin
from travel.models import City, Country, TravelAgency

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(TravelAgency)
class TravelAgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')