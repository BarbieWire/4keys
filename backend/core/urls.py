from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

import core.settings.settings as settings

from application import urls as main_urls
from authentication import urls as auth_urls


handler404 = "core.utils.exception_handlers.error404_hadler"

urlpatterns = [
    # default admin panel
    path('admin/', admin.site.urls),

    # application app
    path('api/', include(main_urls)),

    # all auth paths
    path('api/auth/', include(auth_urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
