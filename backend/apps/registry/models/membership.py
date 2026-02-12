from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedUUIDModel

from .organization import Organization
from .person import Person
from .post import Post


class SelectionMethod(models.TextChoices):
    ELECTED = "elected", _("Elected")
    APPOINTED = "appointed", _("Appointed")
    EX_OFFICIO = "ex_officio", _("Ex Officio")
    HEREDITARY = "hereditary", _("Hereditary")
    UNKNOWN = "unknown", _("Unknown")


class Membership(TimeStampedUUIDModel):
    """
    Represents the relationship between a Person and an Organization/Post.
    This is the core 'tenure' record.
    """

    person = models.ForeignKey(
        Person,
        verbose_name=_("Person"),
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name=_("Organization"),
        on_delete=models.CASCADE,
        related_name="memberships",
        help_text=_("The organization the person belongs" "to (e.g., The Parliament)."),
    )
    post = models.ForeignKey(
        Post,
        verbose_name=_("Post"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="memberships",
        help_text=_(
            "The specific post held (e.g., 'MP for Lagos West')."
            "Optional if generic membership."
        ),
    )
    party = models.ForeignKey(
        Organization,
        verbose_name=_("Party Affiliation"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="party_memberships",
        help_text=_(
            "The political party the person belonged "
            "to during this specific membership."
        ),
    )
    start_date = models.DateField(
        verbose_name=_("Start Date"),
        blank=True,
        null=True,
        help_text=_("The date the person took office."),
    )
    end_date = models.DateField(
        verbose_name=_("End Date"),
        blank=True,
        null=True,
        help_text=_("The date the person left office."),
    )
    selection_method = models.CharField(
        verbose_name=_("Selection Method"),
        max_length=50,
        choices=SelectionMethod.choices,
        default=SelectionMethod.UNKNOWN,
        help_text=_(
            "How the person obtained this position" "(e.g., elected vs appointed)."
        ),
    )

    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")
        ordering = ["-start_date"]

    def __str__(self):
        return (
            f"{self.person.name} - {self.organization.name} ({self.start_date or '?'})"
        )
