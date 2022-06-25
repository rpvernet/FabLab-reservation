from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('reservation/', include('reservation.urls')),
    path('machines/', include('machines.urls')),
    path('rougerosebleu/', admin.site.urls),
    path('compte/', include('accounts.urls')),
    path('admin_calendar/', include('admin_calendar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
