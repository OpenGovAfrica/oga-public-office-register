from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedUUIDModel


class Person(TimeStampedUUIDModel):
    """
    Represents a real human being who holds or has held a public office.
    Based on Popolo 'Person' spec.
    """

    name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=512,
        help_text=_("The primary name the person is known by."),
    )
    biography = models.TextField(
        verbose_name=_("Biography"),
        blank=True,
        null=True,
        help_text=_("A short biography or description of the person."),
    )
    birth_date = models.DateField(
        verbose_name=_("Date of Birth"), blank=True, null=True
    )
    death_date = models.DateField(
        verbose_name=_("Date of Death"), blank=True, null=True
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("e.g. Male, Female, etc."),
    )

    # Optional: A generic field for external IDs (like Wikidata Q-ID)
    # We can add specific fields later, but a notes field is good for now.
    summary = models.CharField(
        verbose_name=_("Summary / One-liner"), max_length=1024, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        ordering = ["name"]

    def __str__(self):
        return self.name
