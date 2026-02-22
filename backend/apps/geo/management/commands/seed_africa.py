from django.core.management.base import BaseCommand

from apps.geo.models import GeographicArea


class Command(BaseCommand):
    help = "Seeds the database with 54 African countries"

    def handle(self, *args, **options):
        africa_data = [
            # North Africa
            ("Algeria", "DZA", "north"),
            ("Egypt", "EGY", "north"),
            ("Libya", "LBY", "north"),
            ("Morocco", "MAR", "north"),
            ("Tunisia", "TUN", "north"),
            ("Western Sahara", "ESH", "north"),
            # West Africa
            ("Benin", "BEN", "west"),
            ("Burkina Faso", "BFA", "west"),
            ("Cabo Verde", "CPV", "west"),
            ("Côte d'Ivoire", "CIV", "west"),
            ("Gambia", "GMB", "west"),
            ("Ghana", "GHA", "west"),
            ("Guinea", "GIN", "west"),
            ("Guinea-Bissau", "GNB", "west"),
            ("Liberia", "LBR", "west"),
            ("Mali", "MLI", "west"),
            ("Mauritania", "MRT", "west"),
            ("Niger", "NER", "west"),
            ("Nigeria", "NGA", "west"),
            ("Senegal", "SEN", "west"),
            ("Sierra Leone", "SLE", "west"),
            ("Togo", "TGO", "west"),
            # East Africa
            ("Burundi", "BDI", "east"),
            ("Comoros", "COM", "east"),
            ("Djibouti", "DJI", "east"),
            ("Eritrea", "ERI", "east"),
            ("Ethiopia", "ETH", "east"),
            ("Kenya", "KEN", "east"),
            ("Madagascar", "MDG", "east"),
            ("Malawi", "MWI", "east"),
            ("Mauritius", "MUS", "east"),
            ("Rwanda", "RWA", "east"),
            ("Seychelles", "SYC", "east"),
            ("Somalia", "SOM", "east"),
            ("South Sudan", "SSD", "east"),
            ("Tanzania", "TZA", "east"),
            ("Uganda", "UGA", "east"),
            # Central Africa
            ("Angola", "AGO", "central"),
            ("Cameroon", "CMR", "central"),
            ("Central African Republic", "CAF", "central"),
            ("Chad", "TCD", "central"),
            ("Congo", "COG", "central"),
            ("DR Congo", "COD", "central"),
            ("Equatorial Guinea", "GNQ", "central"),
            ("Gabon", "GAB", "central"),
            ("São Tomé and Príncipe", "STP", "central"),
            # Southern Africa
            ("Botswana", "BWA", "southern"),
            ("Eswatini", "SWZ", "southern"),
            ("Lesotho", "LSO", "southern"),
            ("Namibia", "NAM", "southern"),
            ("South Africa", "ZAF", "southern"),
            ("Zambia", "ZMB", "southern"),
            ("Zimbabwe", "ZWE", "southern"),
        ]

        created_count = 0
        for name, code, region in africa_data:
            obj, created = GeographicArea.objects.get_or_create(
                country_code=code,
                defaults={
                    "name": name,
                    "admin_level": "country",
                    "continent_region": region,
                },
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Successfully seeded {created_count} countries.")
        )
