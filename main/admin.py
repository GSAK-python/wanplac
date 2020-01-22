from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('data', 'godzina')
    list_display = (Order.order_display, 'data')
    search_fields = ('data', 'trasa')


