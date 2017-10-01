from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Examples:
    url(r'^post_locate/$', include('post_locate.urls'))

]
