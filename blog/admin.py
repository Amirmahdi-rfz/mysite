from django.contrib import admin
from blog.models import Person, Post

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    empty_value_display = 'NULL'
    search_fields = ['first_name', 'last_name', 'age']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = 'NULL'
    search_fields = ['title', 'author']
    fields = ('author', 'title', 'content', 'upload_now')
    list_display = ('author', 'title', 'created_date', 'upload_now')