from django.contrib import admin
from django.urls import path, include
from apps.blog.views import openclaw_ingest

urlpatterns = [
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('newsletter/', include('apps.newsletter.urls')),
    path('legal/', include('apps.legal.urls')),
    path('admin/', admin.site.urls),
    # OpenClaw ingest endpoint (canonical path matching the payload contract)
    path('api/ingest/openclaw-post', openclaw_ingest, name='openclaw_ingest_canonical'),
]
