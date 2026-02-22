from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedUUIDModel


class GeographicArea(TimeStampedUUIDModel):
    class AdminLevel(models.TextChoices):
        COUNTRY = "country", _("Country")
        STATE = "state", _("State/Province")
        DISTRICT = "district", _("District")
        CONSTITUENCY = "constituency", _("Constituency")

    class ContinentRegion(models.TextChoices):
        NORTH = "north", _("North Africa")
        WEST = "west", _("West Africa")
        EAST = "east", _("East Africa")
        CENTRAL = "central", _("Central Africa")
        SOUTHERN = "southern", _("Southern Africa")

    name = models.CharField(_("Name"), max_length=255)
    country_code = models.CharField(
        _("Country Code"),
        max_length=3,
        help_text=_("ISO-3166-1 alpha-3 code (e.g., NGA, KEN)"),
    )
    admin_level = models.CharField(
        _("Administrative Level"),
        max_length=20,
        choices=AdminLevel.choices,
        default=AdminLevel.COUNTRY,
    )
    continent_region = models.CharField(
        _("Continent Region"), max_length=20, choices=ContinentRegion.choices
    )

    # PostGIS field for boundaries/locations
    geometry = models.GeometryField(
        _("Geometry"),
        null=True,
        blank=True,
        help_text=_("Spatial boundaries or point location for this area"),
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        help_text=_(
            "The larger area containing this one (e.g., a State containing a District)"
        ),
    )

    class Meta:
        verbose_name = _("Geographic Area")
        verbose_name_plural = _("Geographic Areas")
        ordering = ["country_code", "admin_level", "name"]

    def __str__(self):
        return f"{self.name} ({self.country_code})"
