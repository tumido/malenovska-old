"""Models for general information."""
import os
from django.db import models
from django.conf import settings

from redactor.fields import RedactorField


class TextOptions(models.Model):
    name = models.CharField('Předmět', max_length=200)
    identifier = models.CharField('Identifikator', max_length=200)
    text = models.CharField('Text', max_length=200)

    class Meta:
        verbose_name = 'Nastavení - Text'
        verbose_name_plural = 'Nastavení - Texty'

    def __str__(self):
        return self.name


class MapPoints(models.Model):
    title = models.CharField('Název', max_length=200)
    long = models.CharField('Zeměpisná délka', max_length=200)
    lat = models.CharField('Zeměpisná šířka', max_length=200)

    class Meta:
        verbose_name = 'Bod na mapě'
        verbose_name_plural = 'Nastavení - Mapa'

    def __str__(self):
        return self.title


class Harmonogram(models.Model):
    program = models.CharField('Program', max_length=200)
    time_start = models.TimeField('Čas začátku')
    time_end = models.TimeField('Čas konce', null=True, blank=True)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Harmonogram'

    def __str__(self):
        return self.program


class ExtraFiles(models.Model):
    name = models.CharField('Titulek', max_length=200)
    tooltip = models.CharField('Popisek', max_length=200)
    filefield = models.FileField('Soubor', blank=True)
    __original_file = None

    class Meta:
        verbose_name = 'Soubor'
        verbose_name_plural = 'Nahrané soubory'

    def __init__(self, *args, **kwargs):
        super(ExtraFiles, self).__init__(*args, **kwargs)
        self.__original_file = self.filefield

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        if self.filefield not in [self.__original_file, '']:
            f_path = os.path.join(settings.MEDIA_ROOT,
                                  str(self.__original_file))

            try:
                os.remove(f_path)
                self.main_file.delete()
            except:
                pass

        super(ExtraFiles, self).save(force_insert, force_update)
        self.__original_file = self.filefield
