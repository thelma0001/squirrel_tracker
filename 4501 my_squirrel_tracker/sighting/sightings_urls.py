from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^sightings/$', views.sightings),
    url(r'^sightings/add$', views.add),
    url(r'^sightings/update$', views.update),
    url(r'^sightings/stats$', views.stats),
    url(r'', views.sightings),
]