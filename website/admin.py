from django.contrib import admin
from website.models import Message

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    empty_value_display = 'NULL'
    search_fields = ['name', 'subject', 'message']
    date_hierarchy = 'created_date'
    list_display = ['name', 'subject', 'created_date', 'status']
    list_filter = ['created_date', 'status']
    fields = ['name', 'subject', 'message',]