from django.shortcuts import render
from django.http import HttpResponse
import os
from . import app_settings

file_path = os.path.abspath(__file__)
directory = os.path.dirname(file_path)

def service_worker(request):
    response = HttpResponse(open(directory+'\\serviceworker.js' , encoding="utf8").read(), content_type='application/javascript')
    return response

def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    }, content_type='application/json')

def offline(request):
    return render(request, "offline.html")

def my_game(request):
    return render(request,'index.html')
def first_page(request):
    return render(request,'TABE.html')
def sec_page(request):
    return render(request,'TSA.html')
def third_page(request):
    return render(request,'geogebra.html')
def forth_page(request):
    return render(request,'TG.html')