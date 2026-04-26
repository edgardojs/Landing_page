from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "source", "is_active", "created_at")
    list_filter = ("is_active", "source")
    search_fields = ("email", "name")
    readonly_fields = ("created_at",)
