from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('newsletter/', include('apps.newsletter.urls')),
    path('legal/', include('apps.legal.urls')),
    path('admin/', admin.site.urls),
]
