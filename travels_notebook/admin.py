from django.contrib import admin
from travels_notebook.models import Places


# Register your models here.

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'time_create', 'time_update', 'relete_user')
