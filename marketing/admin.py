from django.contrib import admin
from .models import BusinessAssociate

@admin.register(BusinessAssociate)
class BusinessAssociateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'fee_ready_to_pay', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_at',)
