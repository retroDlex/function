from django.urls import path , include 
from . import views


urlpatterns = [
    # path('/static/index.html', views.my_game, name='index'),
    path('',  views.my_game),
    # path('sw.js', views.service_worker),
    path('TG.html', views.forth_page),
    path('geogebra.html', views.third_page),
    path('TSA.html', views.sec_page),
    path('TABE.html', views.first_page),
    path('serviceworker.js', views.service_worker, name='serviceworker'),
    path('manifest.json', views.manifest, name='manifest'),
    path('offline.html', views.offline, name='offline')
]