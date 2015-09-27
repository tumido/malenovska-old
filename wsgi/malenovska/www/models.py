from django.db import models
from redactor.fields import RedactorField
from django.core.validators import MinValueValidator

class Race(models.Model):
    name = models.CharField('Jméno rasy', max_length=200)
    description = RedactorField('Popis')
    icon = models.ImageField('Obrázek', blank=True)
    active = models.BooleanField('Letos bojuje')

    class Meta:
        verbose_name = 'Rasa'
        verbose_name_plural = 'Rasy'

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField('Jméno', max_length=200)
    surname = models.CharField('Příjmení', max_length=200)
    nick = models.CharField('Přezdívka', max_length=200)
    age = models.PositiveSmallIntegerField('Věk', validators=[MinValueValidator(10)])
    #email = models.EmailField()
    race = models.ForeignKey(Race, verbose_name='Bojuje za')
    date = models.DateTimeField('Datum registrace')
    ip = models.GenericIPAddressField('IP adresa')

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
    rank = models.PositiveIntegerField('Pozice na strance', primary_key=True)
    name = models.CharField('Nadpis', max_length=200)
    text = RedactorField()

    class Meta:
        verbose_name = 'Panel v "Kontakty" etc.'
        verbose_name_plural = 'Sekce "Kontakty" apod.'

    def __str__(self):
        return self.name
