from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from WhiskeySmash.utils.fight_gen_v2 import fight_setup
# Create your views here.


def home(request):
    context = {'name':'mario'}
    return render(request, 'whiskeywheel/index.html', context)

def wheel(request):
    context = fight_setup(str.title('sokol'), str.title('reen'), str.title('Steve'), str.title('joe'), str.title('bill'))
    return render(request, 'whiskeywheel/wheelpage.html', context)