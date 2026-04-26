from django.contrib import admin
from django.utils import timezone

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "is_published",
        "external_id",
        "published_at",
        "updated_at",
    )
    list_filter = ("status", "is_published")
    search_fields = ("title", "slug", "external_id")
    readonly_fields = ("created_at", "updated_at")
    actions = ("make_published", "make_draft")

    @admin.action(description="Mark selected posts as published (sets published_at to now)")
    def make_published(self, request, queryset):
        now = timezone.now()
        updated = queryset.update(
            status=Post.Status.PUBLISHED,
            is_published=True,
            published_at=now,
        )
        self.message_user(request, f"{updated} post(s) published.")

    @admin.action(description="Mark selected posts as draft (clears published_at)")
    def make_draft(self, request, queryset):
        updated = queryset.update(
            status=Post.Status.DRAFT,
            is_published=False,
            published_at=None,
        )
        self.message_user(request, f"{updated} post(s) set to draft.")
