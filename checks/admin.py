from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Check

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('check_number', 'payer_name', 'amount', 'date_received', 'memo')  # fields to show in list view
    search_fields = ('check_number', 'payer_name')  # enable search
    list_filter = ('date_received',)  # add filter by date
