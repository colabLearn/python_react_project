from django.contrib import admin
from .models import VendorDisc

@admin.register(VendorDisc)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'companyName', 'email')
    search_fields = ('companyName',)

# Register your models here.
