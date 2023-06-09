from django.contrib import admin
from .models import Payment

admin.site.site_header = "Payment Gateway App"
admin.site.site_title = "Billing App Admin Portal"
admin.site.index_title = "Welcome to Payment Gateway by Sanjay"

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'transaction_id', 'paid', 'date']
    date_hierarchy = 'date'
    search_fields = ('amount', 'transaction_id')
    ordering = ['-id']
    list_filter = ('paid', )