from django.shortcuts import render, redirect
from .models import Subscriber


def signup(request):
    """Newsletter signup with HTMX support"""
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        source = request.POST.get('source', 'inline')

        if not email:
            if request.headers.get('HX-Request'):
                response = render(request, 'newsletter/partials/error.html', {
                    'message': 'Please enter a valid email address.'
                })
                response.status_code = 400
                return response
            return render(request, 'newsletter/signup.html', {
                'error': 'Please enter a valid email address.'
            }, status=400)

        subscriber, created = Subscriber.objects.get_or_create(
            email=email,
            defaults={'name': name, 'source': source}
        )

        if request.headers.get('HX-Request'):
            return render(request, 'newsletter/partials/success.html', {
                'email': email,
                'created': created
            })

        return redirect('newsletter_thanks')

    return render(request, 'newsletter/signup.html')


def thanks(request):
    """Newsletter thanks page"""
    return render(request, 'newsletter/thanks.html')
