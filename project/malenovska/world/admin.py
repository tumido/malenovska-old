from django.contrib import admin

from .models import Race


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('name', 'active', 'limit')]}),
        ('Popis', {
            'fields': ['icon', 'fraction', 'description'],
            'classes': ['collapse']
        }),
    ]
    list_display = ['name', 'active', 'limit']
