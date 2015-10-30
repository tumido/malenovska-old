from django.db import models
from redactor.fields import RedactorField
from django.core.validators import MinValueValidator
import os
from django.conf import settings

class Race(models.Model):
    name = models.CharField('Jméno rasy', max_length=200)
    description = RedactorField('Popis', blank=True)
    icon = models.ImageField('Obrázek', upload_to='race_img/', blank=True)
    active = models.BooleanField('Letos bojuje')
    fraction = models.PositiveSmallIntegerField('Frakce')
    limit = models.PositiveSmallIntegerField('Max. hráčů')

    class Meta:
        verbose_name = 'Rasa'
        verbose_name_plural = 'Rasy'

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField('Jméno', max_length=200)
    surname = models.CharField('Příjmení', max_length=200)
    nick = models.CharField('Přezdívka', max_length=200, null=True, blank=True)
    age = models.PositiveSmallIntegerField('Věk', validators=[MinValueValidator(10)])
    #email = models.EmailField()
    race = models.ForeignKey(Race, verbose_name='Bojuje za')
    date = models.DateTimeField('Datum registrace')
    ip = models.GenericIPAddressField('IP adresa')
    group = models.CharField('Skupina', max_length=200, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=200)

    class Meta:
        verbose_name = 'Ragistrovaný hráč'
        verbose_name_plural = 'Registrovaní hráči'
        unique_together = (('name', 'surname', 'nick'),)

    def __str__(self):
        return '{0}: {1} "{2}" {3}'.format(self.race, self.name, self.nick, self.surname)


class Legend(models.Model):
    name = models.CharField('Název', max_length=200)
    text = RedactorField()
    race = models.ForeignKey(Race, verbose_name='Týká se rasy')

    class Meta:
        verbose_name = 'Legenda'
        verbose_name_plural = 'Legendy'

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField('Nadpis', max_length=200)
    text = RedactorField()
    date = models.DateTimeField('Datum vydání')

    class Meta:
        verbose_name = 'Novinka'
        verbose_name_plural = 'Novinky'

    def __str__(self):
        return self.name


class AboutWidget(models.Model):
    name = models.CharField('Nadpis', max_length=200)
    identifier = models.CharField('Identifikator pro stranku', max_length=200)
    text = RedactorField()

    class Meta:
        verbose_name = 'Panely a texty všude možně'
        verbose_name_plural = 'Panely a texty všude možně'

    def __str__(self):
        return self.name


class DateOptions(models.Model):
    name = models.CharField('Událost', max_length=200)
    identifier = models.CharField('Identifikator', max_length=200)
    date = models.DateTimeField('Datum')

    class Meta:
        verbose_name = 'Nastavení - Datum'
        verbose_name_plural = 'Nastavení - Data'

    def __str__(self):
        return self.name


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
        if self.filefield != self.__original_file and self.__original_file != '':
            f_path = os.path.join(settings.MEDIA_ROOT, str(self.__original_file))
 
            try:
                os.remove(f_path)
                self.main_file.delete()
            except:
                pass

        super(ExtraFiles, self).save(force_insert, force_update)
        self.__original_file = self.filefield