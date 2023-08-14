import uuid
from django.db import models
from small_auth.models import BaseUser

MAX_URL_LENTH = 32779 # TODO: If you want to support more up to 64k, you need to re design!

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    url = models.URLField(
        blank=False,
        null=False,
        max_length=MAX_URL_LENTH
    )

