from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='newsletter_signup'),
    path('thanks/', views.thanks, name='newsletter_thanks'),
]
