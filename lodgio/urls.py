from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),

    path('search/', include('search.urls')),
    path('approvals/', include('approvals.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('identity_document/', include('identity_document.urls')),
    path('communications/', include('communications.urls')),
    path('report_ticket/', include('report_ticket.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)