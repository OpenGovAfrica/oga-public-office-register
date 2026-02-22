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


class ChamberType(models.TextChoices):
    """Specific to legislatures to distinguish bicameral systems."""

    UNICAMERAL = "unicameral", _("Unicameral")
    LOWER = "lower_chamber", _("Lower Chamber")
    UPPER = "upper_chamber", _("Upper Chamber")
    NONE = "none", _("Non-Legislative")


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
    chamber_type = models.CharField(
        verbose_name=_("Chamber Type"),
        max_length=20,
        choices=ChamberType.choices,
        default=ChamberType.NONE,
        help_text=_("If this is a legislature, specify the type of chamber."),
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Organization"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        help_text=_(
            "The organization that contains this one "
            "(e.g., a committee within a parliament)."
        ),
    )
    country_code = models.CharField(
        verbose_name=_("Country Code"),
        max_length=3,
        help_text=_("ISO 3166-1 alpha-3 code (e.g., NGA, ZAF, KEN)."),
    )

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ["country_code", "name"]  # Group by country first

    def __str__(self):
        return f"{self.name} ({self.country_code})"
