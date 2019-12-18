from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User


class Room(models.Model):

    class Status(models.IntegerChoices):
        ACTIVE = 0, _('Active')
        PLAYED = 1, _('PLAYED')
        DONE = 2, _('DONE')

    class Figure(models.IntegerChoices):
        SQUARE = 0, _('SQUARE')
        TRIANGLE_1 = 1, _('TRIANGLE_TYPE_1')
        TRIANGLE_2 = 2, _('TRIANGLE_TYPE_2')
        TRIANGLE_3 = 3, _('TRIANGLE_TYPE_3')

    user_count = models.IntegerField()
    status = models.IntegerField(choices=Status.choices)
    figure = models.IntegerField(choices=Figure.choices)

    players = models.ManyToManyField(User, through='room.UserJoin', through_fields=('room', 'user'), related_name='rooms')

    def __str__(self):
        return f'Room Count: {self.user_count}; Figure: {self.figure}; Status: {self.status}'


class Dot(models.Model):
    abscissa = models.DecimalField(help_text='x', max_digits=10, decimal_places=10)
    ordinate = models.DecimalField(help_text='y', max_digits=10, decimal_places=10)

    def __str__(self):
        return f'X: {self.abscissa}; Y: {self.ordinate}'


class UserJoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    dot = models.ForeignKey(Dot, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'room')
