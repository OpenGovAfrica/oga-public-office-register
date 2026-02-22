from django.test import TestCase

from apps.geo.models import GeographicArea
from apps.registry.models.organization import (
    ChamberType,
    Organization,
    OrganizationType,
)
from apps.registry.models.post import Post, PostType


class StructuralIntegrityTest(TestCase):
    def setUp(self):
        # 1. Setup a Country 'Anchor'
        self.ghana = GeographicArea.objects.create(
            name="Ghana",
            country_code="GHA",
            admin_level="country",
            continent_region="west",
        )

        # 2. Setup a Hierarchy (Constituency -> Country)
        self.accra = GeographicArea.objects.create(
            name="Accra Central",
            country_code="GHA",
            admin_level="constituency",
            parent=self.ghana,
            continent_region="west",
        )

    def test_bicameral_modeling(self):
        """Test Phase 1.3: Modeling a Parliament with child Chambers."""
        parliament = Organization.objects.create(
            name="Parliament of Ghana",
            classification=OrganizationType.LEGISLATURE,
            country_code="GHA",
        )
        # Testing the new chamber_type field
        chamber = Organization.objects.create(
            name="National Assembly",
            classification=OrganizationType.LEGISLATURE,
            chamber_type=ChamberType.UNICAMERAL,
            parent=parliament,
            country_code="GHA",
        )

        self.assertEqual(chamber.parent.name, "Parliament of Ghana")
        self.assertEqual(chamber.chamber_type, ChamberType.UNICAMERAL)
        self.assertIn(chamber, parliament.children.all())

    def test_post_to_geo_resolution(self):
        """Test Phase 1.2: Verify Post links correctly to GeographicArea."""
        org = Organization.objects.create(name="Gov", country_code="GHA")
        post = Post.objects.create(
            label="MP for Accra Central",
            role_type=PostType.LEGISLATIVE,
            organization=org,
            area=self.accra,  # Link to the new Geo model
        )

        # Verify traversal: Post -> Area -> Parent Country
        self.assertEqual(post.area.name, "Accra Central")
        self.assertEqual(post.area.parent.country_code, "GHA")

    def test_enum_enforcement(self):
        """Test Phase 1.4: Ensure controlled vocabulary is used."""
        org = Organization.objects.create(name="Gov", country_code="GHA")
        post = Post.objects.create(
            label="Chief Justice", role_type=PostType.JUDICIAL, organization=org
        )
        # This confirms our PostType enum is working in the DB
        self.assertEqual(post.role_type, PostType.JUDICIAL)
