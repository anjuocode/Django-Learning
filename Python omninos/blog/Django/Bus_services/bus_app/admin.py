from django.contrib import admin
from.models import Bus
# Register your models here.
admin.site.register(Bus)
class Bus(admin.ModelAdmin):
    list_display = ['passenger_name','passender_id','bus_name','where','to']