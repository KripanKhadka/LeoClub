from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .leo_views import about, events, home, join, membership_application

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("events/", events, name="events"),
    path("join/", join, name="join"),
    path("join/apply/", membership_application, name="membership_application"),
]

# Serves uploaded media locally during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)