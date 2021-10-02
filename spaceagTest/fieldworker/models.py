import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FieldWorker(models.Model):

    class Activity(models.TextChoices):
        HARVEST = 'HA', _('Harvest')
        PRUNING = 'PR', _('Pruning')
        SCOUNTING = 'SC', _('Scouting')
        OTHER = 'OT', _('Other')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    function = models.CharField(
        max_length=2, choices=Activity.choices, default=Activity.OTHER,)
    created_at = models.DateTimeField(auto_now_add=True)
