from django.db import models
from redactor.fields import RedactorField

from world.models import Race


class Legend(models.Model):
    name = models.CharField('Název', max_length=200)
    text = RedactorField()
    race = models.ForeignKey(Race, verbose_name='Týká se rasy')

    class Meta:
        verbose_name = 'Legenda'
        verbose_name_plural = 'Legendy'

    def __str__(self):
        return self.name
