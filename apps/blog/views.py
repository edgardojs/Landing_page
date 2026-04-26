import json
import secrets

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Post


# ---------------------------------------------------------------------------
# Public blog pages
# ---------------------------------------------------------------------------

def post_list(request):
    """Blog list page with categories"""
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, slug):
    """Blog detail page with newsletter CTA"""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'blog/detail.html', {'post': post})


# ---------------------------------------------------------------------------
# OpenClaw webhook ingest
# ---------------------------------------------------------------------------

def _bearer_ok(request) -> bool:
    """Validate the Authorization: Bearer <token> header."""
    token = settings.OPENCLAW_WEBHOOK_TOKEN
    if not token:
        return False
    auth = request.headers.get("Authorization", "")
    expected = f"Bearer {token}"
    return secrets.compare_digest(auth, expected)


def _json_body(request):
    """Parse JSON body; return (data, None) or (None, error_response)."""
    ctype = request.headers.get("Content-Type", "")
    if ctype:
        base = ctype.split(";")[0].strip().lower()
        if base != "application/json":
            return None, JsonResponse(
                {"error": "Content-Type must be application/json"},
                status=415,
            )
    try:
        return json.loads(request.body.decode("utf-8")), None
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None, JsonResponse({"error": "invalid JSON body"}, status=400)


@csrf_exempt
@require_POST
def openclaw_ingest(request):
    """
    Machine ingest endpoint: always stores as draft.
    Upserts on external_id so retries are idempotent.
    """
    if not _bearer_ok(request):
        return JsonResponse({"error": "unauthorized"}, status=401)

    data, err = _json_body(request)
    if err:
        return err

    external_id = data.get("external_id")
    title = data.get("title")
    body_markdown = data.get("body_markdown")
    if not external_id or not title or not body_markdown:
        return JsonResponse(
            {
                "error": "missing required fields",
                "required": ["external_id", "title", "body_markdown"],
            },
            status=400,
        )

    tags = data.get("tags") if isinstance(data.get("tags"), list) else []
    meta_in = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    meta = {**meta_in, "ingest": "openclaw_webhook"}
    excerpt = data.get("excerpt", "")

    slug = Post.slug_from_title_and_external_id(title, external_id)

    post, created = Post.objects.get_or_create(
        external_id=external_id,
        defaults={
            "title": title,
            "slug": slug,
            "body_markdown": body_markdown,
            "content": body_markdown,
            "excerpt": excerpt,
            "status": Post.Status.DRAFT,
            "is_published": False,
            "published_at": None,
            "tags": tags,
            "meta": meta,
        },
    )
    if not created:
        post.title = title
        post.slug = slug
        post.body_markdown = body_markdown
        post.content = body_markdown
        post.excerpt = excerpt
        post.status = Post.Status.DRAFT
        post.is_published = False
        post.published_at = None
        post.tags = tags
        post.meta = meta
        post.save()

    status_code = 201 if created else 200
    return JsonResponse(
        {
            "ok": True,
            "created": created,
            "id": post.id,
            "external_id": post.external_id,
            "slug": post.slug,
            "status": post.status,
        },
        status=status_code,
    )
