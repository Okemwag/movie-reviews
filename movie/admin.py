from django.contrib import admin
from . import models

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year', 'created_at', 'updated_at')
    list_filter = ('year', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-year', 'title')
    
admin.site.register(models.Movie, MovieAdmin)
