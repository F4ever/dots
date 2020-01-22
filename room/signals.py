from django.db.models.signals import post_save
from django.dispatch import receiver

from room.models import UserJoin
from room.services import RoomCalculationService


@receiver(post_save, sender=UserJoin)
def check_room(sender, **kwargs):
    rcs = RoomCalculationService(room=sender.room_id)
    rcs.calculate_results()