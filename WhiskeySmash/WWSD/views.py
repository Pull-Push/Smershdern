from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .import demo
# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    context = {
        'chars':demo.chars
    }
    return HttpResponse(template.render(context, request))