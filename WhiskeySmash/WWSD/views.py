from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

char_list = ['mario', 'luigi','ponch', 'lonk']

def home(request):
    template = loader.get_template('index.html')
    context = {
        'chars':char_list
    }
    return HttpResponse(template.render(context, request))