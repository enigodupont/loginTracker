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
from django.views.decorators.csrf import csrf_exempt
import requests

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
            'title':'About Us',
            'message':'A Login Tracker made by Juan Carlos Ramirez & Marvin Leister.',
            'year':datetime.now().year,
        }
    )

@csrf_exempt
def locate(request):
    assert isinstance(request, HttpRequest)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR');
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    
    url="http://api.ipstack.com/"+client_ip+"?access_key=3dd7389caccffbde5be84d694bb34616"
    r = requests.get(url)
    js = r.json()
    local = locationData()
    local.lat = js['latitude']
    local.long = js['longitude']
    local.ip = client_ip
    local.logDate = datetime.now()

    if local.lat == None or local.long == None:
        local.lat = 0;
        local.long = 0;
    if request.method == "POST":
        try:
            user = authenticate(username=request.POST['user'],password=request.POST['pass'])
            local.user = user
            local.save()
            return render(request,'app/client_pass.html')
        except:
            pass
    if request.method == "GET":
        if request.user.is_authenticated():
            local.user = request.user
            local.save()
    return render(request,'app/locate.html')
