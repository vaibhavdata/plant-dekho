from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('bosslogin/', admin.site.urls),
    path('', include('nursery_ecommerce_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admindashboard/',include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
