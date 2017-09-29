from django.contrib import admin

from .models import TextOptions, Harmonogram, MapPoints, ExtraFiles


@admin.register(ExtraFiles)
class FilesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('name', 'tooltip', 'filefield')]}),
    ]


@admin.register(TextOptions)
class TextOptionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('name', 'text')]}),
        ('Skryto', {'fields': ['identifier'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'text']


@admin.register(MapPoints)
class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('title', 'lat', 'long')]}),
    ]


@admin.register(Harmonogram)
class HarmonogramAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
         ('program', 'time_start', 'time_end')]}),
    ]
    list_display = ['time_start', 'time_end', 'program']
