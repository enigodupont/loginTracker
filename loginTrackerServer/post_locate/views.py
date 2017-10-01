from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def locate(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'post_locate/locate.html',
        {
            'title': 'locate',
            'ip_addr': request.META['REMOTE_ADDR']
        }
    )
