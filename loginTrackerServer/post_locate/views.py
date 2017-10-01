from django.shortcuts import render
from django.http import HttpRequest
import requests
from app.models import locationData
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

# Create your views here.

@csrf_exempt
def locate(request):
    assert isinstance(request, HttpRequest)
    client_ip = request.META['REMOTE_ADDR']
    url="http://freegeoip.net/json/"+client_ip
    r = requests.get(url)
    js = r.json()
    local = locationData()
    local.lat = js['latitude']
    local.long = js['longitude']


    user = authenticate(username=request.POST['user'],password=request.POST['pass'])
    local.user = user
    local.save()
    
    
    return render(
        request,
        'post_locate/locate.html',
        {
            'title'       : 'locate',
            'lat'         : js['latitude'],
            'long'        : js['longitude'],
            'city'        : js['city'],
            'country_name': js['country_name'],
            'user'        : request.POST['user']
        }
    )
