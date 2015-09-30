from django.contrib import admin
from django.http import HttpResponse
from .models import Race, Player, Legend, News, AboutWidget, DateOptions, TextOptions, MapPoints

def export_xlsx(modeladmin, request, queryset):
    import openpyxl
    from openpyxl.cell import get_column_letter
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=registrace.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.get_active_sheet()
    ws.title = "Registrovaní hráči"

    row_num = 0

    columns = [
        (u"Rasa", 20),
        (u"Přezdívka", 20),
        (u"Jméno", 20),
        (u"Příjmení", 20)
    ]

    for col_num in range(len(columns)):
        c = ws.cell(row=row_num + 1, column=col_num + 1)
        c.value = columns[col_num][0]
        c.style.font.bold = True
        # set column width
        ws.column_dimensions[get_column_letter(col_num+1)].width = columns[col_num][1]

    for obj in queryset.order_by('-race'):
        row_num += 1
        row = [obj.race.name,
               obj.nick,
               obj.name,
               obj.surname]
        for col_num in range(len(row)):
            c = ws.cell(row=row_num + 1, column=col_num + 1)
            c.value = row[col_num]
            c.style.alignment.wrap_text = True

    wb.save(response)
    return response

export_xlsx.short_description = u"Exportovat jako XLSX (Excel)"

class PlayerAdmin(admin.ModelAdmin):
    actions = [export_xlsx]
    fieldsets = [
        (None,               {'fields': [('nick', 'name', 'surname'), ('race', 'age')]}),
        ('Detaily', {'fields': ['email', 'date', 'ip'], 'classes': ['collapse']}),
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

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [('title', 'lat', 'long')]}),
    ]

admin.site.register(Race, RaceAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Legend, LegendAdmin)
admin.site.register(News)
admin.site.register(AboutWidget)
admin.site.register(MapPoints,MapAdmin)
admin.site.register(DateOptions, DateOptionsAdmin)
admin.site.register(TextOptions, TextOptionsAdmin)