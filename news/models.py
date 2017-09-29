"""News model."""
from django.db import models
from redactor.fields import RedactorField


class News(models.Model):
    """News model for Malenovska home page."""

    name = models.CharField('Nadpis', max_length=200)
    text = RedactorField()
    date = models.DateTimeField('Datum vydání')

    class Meta:
        """Django Meta class."""
        verbose_name = 'Novinka'
        verbose_name_plural = 'Novinky'

    def __str__(self):
        """String representation displayed in admin."""
        return self.name
