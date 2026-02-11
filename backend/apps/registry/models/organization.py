from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedUUIDModel


class OrganizationType(models.TextChoices):
    LEGISLATURE = "legislature", _("Legislature")
    EXECUTIVE = "executive", _("Executive Body")
    JUDICIARY = "judiciary", _("Judiciary")
    PARTY = "party", _("Political Party")
    MINISTRY = "ministry", _("Ministry")
    COMMITTEE = "committee", _("Committee")
    UNKNOWN = "unknown", _("Unknown")


class Organization(TimeStampedUUIDModel):
    """
    Represents a group of people with a common purpose,
    such as a legislature, a political party, or a government department.
    """

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=512,
        help_text=_("The official name of the organization."),
    )
    classification = models.CharField(
        verbose_name=_("Classification"),
        max_length=50,
        choices=OrganizationType.choices,
        default=OrganizationType.UNKNOWN,
        help_text=_("The category of the organization (e.g., Legislature, Party)."),
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Organization"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        help_text=_(
            "The organization that contains this one"
            "(e.g., a committee within a parliament)."
        ),
    )
    # We will refine this field in Phase 1.2 with a proper GeographicArea model,
    # but for now, we stick to the basic ISO code as a placeholder.
    country_code = models.CharField(
        verbose_name=_("Country Code"),
        max_length=3,
        help_text=_("ISO 3166-1 alpha-3 code (e.g., NGA, ZAF, KEN)."),
    )

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.get_classification_display()})"
