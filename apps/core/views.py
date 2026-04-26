from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import ContactMessage
from apps.newsletter.models import Subscriber


def home(request):
    """Home page with hero, features, featured blog posts, inline newsletter"""
    from apps.blog.models import Post
    featured_posts = Post.objects.filter(is_published=True)[:3]
    return render(request, 'core/home.html', {'featured_posts': featured_posts})


def about(request):
    """About page with mission, story, brand info"""
    return render(request, 'core/about.html')


def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            if request.headers.get('HX-Request'):
                return render(request, 'core/partials/contact_success.html')
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
    
    return render(request, 'core/contact.html')


def landing(request):
    """Landing page with focused CTA, benefits, testimonials, FAQ"""
    return render(request, 'core/landing.html')
