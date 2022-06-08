from django.contrib import admin
from travels_notebook.models import Places


# Register your models here.

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):

