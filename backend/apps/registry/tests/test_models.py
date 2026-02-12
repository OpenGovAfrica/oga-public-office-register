from django.test import TestCase

from apps.registry.models import (
    Membership,
    Organization,
    OrganizationType,
    Person,
    Post,
    PostType,
    SelectionMethod,
)


class RegistryModelTests(TestCase):
    def setUp(self):
        # 1. Create an Organization (The Parliament)
        self.parliament = Organization.objects.create(
            name="National Assembly",
            classification=OrganizationType.LEGISLATURE,
            country_code="NGA",
        )

        # 2. Create a Post (Speaker)
        self.speaker_post = Post.objects.create(
            label="Speaker of the House",
            role_type=PostType.LEGISLATIVE,
            organization=self.parliament,
        )

        # 3. Create a Person (Hon. John Doe)
        self.person = Person.objects.create(
            name="John Doe", gender="Male", birth_date="1980-01-01"
        )

    def test_organization_creation(self):
        """Test that organization is created with correct defaults"""
        self.assertEqual(self.parliament.country_code, "NGA")
        self.assertEqual(self.parliament.classification, OrganizationType.LEGISLATURE)
        self.assertTrue(str(self.parliament).startswith("National Assembly"))

    def test_post_creation(self):
        """Test that post is linked to organization"""
        self.assertEqual(self.speaker_post.organization, self.parliament)
        self.assertEqual(self.speaker_post.role_type, PostType.LEGISLATIVE)

    def test_membership_linkage(self):
        """Test linking a Person to a Post via Membership"""
        membership = Membership.objects.create(
            person=self.person,
            organization=self.parliament,
            post=self.speaker_post,
            start_date="2023-05-29",
            selection_method=SelectionMethod.ELECTED,
        )

        # Verify the links work both ways
        self.assertEqual(membership.person.name, "John Doe")
        self.assertEqual(membership.post.label, "Speaker of the House")

        # Test Reverse Relationship (Accessing memberships from the Person)
        self.assertEqual(self.person.memberships.count(), 1)
        self.assertEqual(self.person.memberships.first(), membership)

    def test_organization_hierarchy(self):
        """Test that an organization can have a parent (e.g. Committee -> Parliament)"""
        # Create a Committee
        committee = Organization.objects.create(
            name="Committee on Public Accounts",
            classification=OrganizationType.COMMITTEE,
            parent=self.parliament,  # Link to the Parliament created in setUp
            country_code="NGA",
        )

        self.assertEqual(committee.parent, self.parliament)
        self.assertIn(committee, self.parliament.children.all())
