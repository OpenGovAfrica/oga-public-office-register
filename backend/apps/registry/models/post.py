from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedUUIDModel

from .organization import Organization


class PostType(models.TextChoices):
    LEGISLATIVE = "legislative", _("Legislative")
    EXECUTIVE = "executive", _("Executive")
    JUDICIAL = "judicial", _("Judicial")
    LOCAL_GOVT = "local_government", _("Local Government")
    TRADITIONAL = "traditional_authority", _("Traditional Authority")
    UNKNOWN = "unknown", _("Unknown")


class Post(TimeStampedUUIDModel):
    """
    Represents a position that exists in an organization, regardless
    of who holds it (e.g., 'MP for Constituency A', 'Minister of Finance').
    """

    label = models.CharField(
        verbose_name=_("Label"),
        max_length=512,
        help_text=_("The name of the office (e.g., 'Senator for Lagos West')."),
    )
    role_type = models.CharField(
        verbose_name=_("Role Type"),
        max_length=50,
        choices=PostType.choices,
        default=PostType.UNKNOWN,
        help_text=_("The branch of government or type of authority."),
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name=_("Organization"),
        on_delete=models.CASCADE,
        related_name="posts",
        help_text=_("The body where this post exists (e.g., The Senate)."),
    )
    # Note: In Phase 1.2, we will add a ForeignKey to GeographicArea here.
    # For now, the 'label' usually contains the geographic context.

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["label"]

    def __str__(self):
        return f"{self.label} ({self.organization.name})"
