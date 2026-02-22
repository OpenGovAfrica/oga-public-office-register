from django.contrib.gis import admin

from .models import GeographicArea


@admin.register(GeographicArea)
class GeographicAreaAdmin(admin.GISModelAdmin):
    list_display = ("name", "country_code", "admin_level", "continent_region")
    list_filter = ("country_code", "admin_level", "continent_region")
    search_fields = ("name",)
    # This enables the OpenStreetMap widget in the admin
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 4,
            "default_lat": 0,
            "default_lon": 20,
        }
    }
