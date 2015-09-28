from django.contrib import admin
from .models import Race, Player, Legend, News, AboutWidget, DateOptions, TextOptions

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('nick', 'name', 'surname'), ('race', 'age')]}),
        ('Detaily', {'fields': ['date', 'ip'], 'classes': ['collapse']}),
    ]
class RaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('name', 'active', 'limit')]}),
        ('Popis', {'fields': ['icon', 'fraction', 'description'], 'classes': ['collapse']}),
    ]


class LegendAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('name', 'race'), 'text']}),
    ]

class DateOptionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('name', 'identifier'), 'date']}),
    ]

class TextOptionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('name', 'identifier'), 'text']}),
    ]

admin.site.register(Race, RaceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Legend, LegendAdmin)
admin.site.register(News)
admin.site.register(AboutWidget)
admin.site.register(DateOptions, DateOptionsAdmin)
admin.site.register(TextOptions, TextOptionsAdmin)