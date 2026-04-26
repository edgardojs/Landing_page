from django.shortcuts import render


def privacy(request):
    """Privacy policy page"""
    return render(request, 'legal/privacy.html')


def terms(request):
    """Terms of service page"""
    return render(request, 'legal/terms.html')
