from django.contrib import admin
from .models import LatestNews

# Register your models here.
@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'image', 'date', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active',)
    ordering = ('-date',)
