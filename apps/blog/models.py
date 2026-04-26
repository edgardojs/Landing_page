import hashlib

from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    # Core fields
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)
    body_markdown = models.TextField(blank=True, default="")
    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True)

    # Status & publishing
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    # OpenClaw ingest fields
    external_id = models.CharField(
        max_length=200, unique=True, blank=True, null=True,
        help_text="Stable ID for OpenClaw upserts / retries.",
    )
    tags = models.JSONField(default=list, blank=True)
    meta = models.JSONField(default=dict, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) or "post"
        # Keep is_published in sync with status for backward compatibility
        if self.status == self.Status.PUBLISHED:
            self.is_published = True
        else:
            self.is_published = False
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("blog_detail", kwargs={"slug": self.slug})

    @staticmethod
    def slug_from_title_and_external_id(title: str, external_id: str) -> str:
        base = (slugify(title) or "post")[:140]
        digest = hashlib.sha256(external_id.encode()).hexdigest()[:10]
        return f"{base}-{digest}"[:200]
