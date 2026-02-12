from django.contrib import admin

from .models import Membership, Organization, Person, Post


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "birth_date", "id")
    search_fields = ("name",)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "classification", "country_code", "parent")
    list_filter = ("classification", "country_code")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("label", "organization", "role_type")
    list_filter = ("role_type", "organization")
    search_fields = ("label",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("person", "organization", "post", "start_date", "end_date")
    list_filter = ("selection_method", "start_date")
    search_fields = ("person__name", "organization__name", "post__label")
