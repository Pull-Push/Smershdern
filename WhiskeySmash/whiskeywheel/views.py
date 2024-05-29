from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from WhiskeySmash.utils.fight_gen_v3 import fight_setup
# Create your views here.


# def home(request):
#     context = {'name':'mario'}
#     return render(request, 'whiskeywheel/index.html', context)

def wheel(request):
    return render(request, 'whiskeywheel/wheelpage.html')

def wheelsend(request):
    fighter1 = request.POST['fight1']
    fighter2 = request.POST['fight2']
    fighter3 = request.POST['fight3']
    fighter4 = request.POST['fight4']
    fighter5 = request.POST['fight5']
    fighter6 = request.POST['fight6']
    context = fight_setup(str.title(fighter1),str.title(fighter2),str.title(fighter3), str.title(fighter4), str.title(fighter5), str.title(fighter6))
    return render(request, 'whiskeywheel/wheelpage.html', context)