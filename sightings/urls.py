from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index),
    #path('', views.main),
    path('', views.list),
    path('stats', views.stats),
    path('<unique_squirrel_id>', views.update),
]

