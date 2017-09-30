"""
Definition of urls for loginTrackerServer.
"""

from datetime import datetime
from django.urls import include, re_path
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    re_path(r'^$', app.views.home, name='home'),
    re_path(r'^contact$', app.views.contact, name='contact'),
    re_path(r'^about', app.views.about, name='about'),
    re_path(r'^map', app.views.map, name='map'),
    re_path(r'^signup/$', app.views.signup, name='signup'),
    re_path(r'^locate/$', app.views.locate, name='locate'),
    re_path(r'^login/$',
        django.contrib.auth.views.LoginView.as_view(
            template_name ='app/login.html',
            authentication_form = app.forms.BootstrapAuthenticationForm,
            extra_context =
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        ),
        name='login'),
    re_path(r'^logout$',
        django.contrib.auth.views.LogoutView.as_view(
            next_page = '/',
        ),
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # re_path(r'^admin/', include(admin.site.urls)),
]
