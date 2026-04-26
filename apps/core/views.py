from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


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

        if not (name and email and message):
            context = {
                'error': 'Name, email, and message are required.',
                'form': {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message,
                }
            }
            template = 'core/partials/contact_form.html' if request.headers.get('HX-Request') else 'core/contact.html'
            response = render(request, template, context)
            response.status_code = 400
            return response

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

    if request.headers.get('HX-Request'):
        return render(request, 'core/partials/contact_form.html')

    return render(request, 'core/contact.html')


def landing(request):
    """Landing page with focused CTA, benefits, testimonials, FAQ"""
    return render(request, 'core/landing.html')
