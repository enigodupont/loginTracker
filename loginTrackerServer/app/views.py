"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from datetime import datetime

from app.forms import SignUpForm
from app.models import locationData

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def map(request):
    """Renders the map page."""
    assert isinstance(request, HttpRequest)
    all_locations = []
    all_locations = locationData.objects.filter(user_id=request.user.id)
    return render(
        request,
        'app/map.html',
        {
            'title':'Location Map',
            'year':datetime.now().year,
            'locations': all_locations,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def signup(request):
    """Renders the signup page."""
    assert isinstance(request,HttpRequest)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            login(request,user)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(
        request,
        'app/signup.html',
        {'form': form,
         'title':"Sign Up",
         'message': "Sign in page",
         'year':datetime.now().year,
         }
        )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
