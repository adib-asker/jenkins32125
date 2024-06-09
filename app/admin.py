from django.contrib import admin
from .models import PhoneBook

@admin.register(PhoneBook)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
