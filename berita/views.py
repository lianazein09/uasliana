from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here
def berita(request):
    template = loader.get_template('berita.html')
    return HttpResponse (template.render())

def detailberita(request):
    template = loader.get_template('detailberita.html')
    return HttpResponse (template.render())

def isiberita(request):
    template = loader.get_template('isiberita.html')
    return HttpResponse (template.render())

def selesai(request):
    template = loader.get_template('selesai.html')
    return HttpResponse (template.render())

def done(request):
    template = loader.get_template('done.html')
    return HttpResponse (template.render())
