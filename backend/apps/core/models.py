import uuid

from django.db import models


class TimeStampedUUIDModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields, and a UUID primary key.
    """

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
