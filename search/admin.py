# admin.py in search application
from django.contrib import admin
from search.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'items')

admin.site.register(Restaurant, RestaurantAdmin)
