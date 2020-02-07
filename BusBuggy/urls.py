from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('accounts.urls', namespace='profiles')),
    path("", include('core.urls', namespace='core')),
    path("", include('hiring.urls', namespace='hire')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
