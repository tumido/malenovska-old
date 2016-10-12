"""Admin interface for registered Players."""
from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from .models import Player


def export_xlsx(modeladmin, request, queryset):
    """Export to XLSX action for list of Players."""
    # import required OpenDocument packages
    from openpyxl import Workbook
    from openpyxl.styles import Font
    from openpyxl.writer.write_only import WriteOnlyCell

    # initialize empty document
    workbook = Workbook(write_only=True)
    sheet = workbook.create_sheet('Registrovaní hráči')

    # update column width
    for item in 'ABCDE':
        sheet.column_dimensions[item].width = 20

    # initialize header
    font = Font(bold=True)
    header = list()
    for item in ['Rasa', 'Přezdívka', 'Jméno', 'Příjmení', 'Věk']:
        cell = WriteOnlyCell(sheet, value=item)
        cell.font = font
        header.append(cell)
    sheet.append(header)

    # populate content
    dataset = queryset.order_by('race', 'nick', 'surname')
    for item in dataset:
        data = [
            item.race.name,
            item.nick,
            item.name,
            item.surname,
            item.age
        ]
        sheet.append(data)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=registrace.xlsx'
    workbook.save(response)

    return response
export_xlsx.short_description = 'Exportovat jako XLSX (Excel)'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Admin UI for Player model."""

    actions = [export_xlsx]
    fieldsets = [
        (None, {
            'fields': [
                ('nick', 'name', 'surname'),
                ('race', 'age')
            ]
        }),
        ('Detaily', {
            'fields': ['email', 'date', 'ip'],
            'classes': ['collapse']
        }),
    ]
    list_display = ['race', 'nick', 'name', 'surname', 'age']
    ordering = ('race', 'nick', 'surname')

    def get_form(self, request, obj=None, **kwargs):
        """Default form values."""
        form = super(PlayerAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['date'].initial = timezone.now()
        form.base_fields['ip'].initial = '0.0.0.0'
        form.base_fields['email'].initial = 'dev-null@malenovska.cz'
        return form
