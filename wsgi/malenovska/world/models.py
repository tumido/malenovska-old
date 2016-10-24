from django.db import models
from redactor.fields import RedactorField


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
