from django.contrib import admin
from .models import Plate


@admin.register(Plate)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'plate_number')
