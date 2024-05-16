from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    context = {'name':'mario'}
    return render(request, 'whiskeywheel/index.html', context)

def wheel(request):
    return render(request, 'whiskeywheel/wheelpage.html')