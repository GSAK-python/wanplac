from django.contrib import admin
from .models import Startowa, Terminy




# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_filter = ('data', 'godzina')
#     list_display = (Order.order_display, 'data')
#     search_fields = ('data', 'trasa')

admin.site.register(Startowa)
admin.site.register(Terminy)
admin.site.register(Terminy.MyOrder)

# admin.site.register(MyOrder2)








