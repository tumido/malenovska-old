"""Models for Players."""

from django.db import models
from django.core.validators import MinValueValidator

from world.models import Race


class Player(models.Model):
    """Player representation in the DB."""

    # Player identification
    name = models.CharField('Jméno', max_length=200)
    surname = models.CharField('Příjmení', max_length=200)
    nick = models.CharField('Přezdívka', max_length=200, null=True, blank=True)

    # Additional personal data
    age = models.PositiveSmallIntegerField(
        'Věk', validators=[MinValueValidator(10)])
    email = models.EmailField('E-mail', max_length=200)

    # Game related info
    group = models.CharField('Skupina', max_length=200, null=True, blank=True)
    race = models.ForeignKey(Race, verbose_name='Bojuje za')

    # Website interest
    date = models.DateTimeField('Datum registrace')
    ip = models.GenericIPAddressField('IP adresa')

    class Meta:
        """Django table metas."""

        verbose_name = 'Ragistrovaný hráč'
        verbose_name_plural = 'Registrovaní hráči'
        unique_together = (('name', 'surname', 'nick'),)

    def __str__(self):
        """String representation of player."""
        return '{0}: {1} "{2}" {3}'.format(
            self.race, self.name, self.nick, self.surname)
