from django.contrib import admin
from . models import Files
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display=('file_name', 'description', 'datetime')
    fields=('file_name', 'file', 'description',)

admin.site.register(Files, FileAdmin)