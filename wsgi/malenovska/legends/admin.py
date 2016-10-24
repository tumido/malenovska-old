from django.contrib import admin

from .models import Legend


@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('name', 'race'), 'text']}),
    ]
