from django.db import models

from redactor.fields import RedactorField


class AboutWidget(models.Model):
    """Model storing the text labels and notes all around the site."""

    name = models.CharField('Nadpis', max_length=200)
    identifier = models.CharField('Identifikator pro stranku', max_length=200)
    text = RedactorField()

    class Meta:
        """"Django meta class name."""

        verbose_name = 'Panely a texty všude možně'
        verbose_name_plural = 'Panely a texty všude možně'

    def __str__(self):
        """"String repr. of AboutWidget."""
        return self.name


class DateOptions(models.Model):
    """"Table for dates."""

    name = models.CharField('Událost', max_length=200)
    identifier = models.CharField('Identifikator', max_length=200)
    date = models.DateTimeField('Datum')

    class Meta:
        """"Django meta class name."""

        verbose_name = 'Nastavení - Datum'
        verbose_name_plural = 'Nastavení - Data'

    def __str__(self):
        """"String repr. of dates."""
        return self.name
