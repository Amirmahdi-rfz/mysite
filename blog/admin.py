from django.contrib import admin
from blog.models import Person

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    empty_value_display = 'NULL'
    search_fields = ['first_name', 'last_name', 'age']


# admin.site.register(Person, PersonAdmin)
