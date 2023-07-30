from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'body', 'date')
    list_filter = ('date',)
    search_fields = ('headline', 'body')
    ordering = ('-date', 'headline')
    
admin.site.register(News)
