from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok", "service": "OGA Public Office Register"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
]
