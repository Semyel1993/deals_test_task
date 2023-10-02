from django.contrib import admin

from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'total', 'quantity', 'date',)
    search_fields = ('customer', 'item',)
