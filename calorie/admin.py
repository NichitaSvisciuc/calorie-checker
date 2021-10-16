from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):

	list_filter = ['name', 'value']
	search_fields = ['name', 'value']


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)