from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

from .views import home


urlpatterns = [
    url(r"^$", home, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^images/", include("pinax.images.urls", namespace="pinax_images")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
