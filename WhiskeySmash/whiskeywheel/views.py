from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from WhiskeySmash.utils.fight_gen_v3 import fight_setup
from WhiskeySmash.utils.home_render import createGrid
# Create your views here.


def home(request):
    return render(request, 'whiskeywheel/index.html')

def grid(request):
    context = createGrid()
    return render(request, 'whiskeywheel/grid.html', context)

def wheel(request):
    return render(request, 'whiskeywheel/wheelpage.html')

def wheelsend(request):
    fighter1 = request.POST['fight1']
    fighter2 = request.POST['fight2']
    fighter3 = request.POST['fight3']
    fighter4 = request.POST['fight4']
    fighter5 = request.POST['fight5']
    fighter6 = request.POST['fight6']
    fighter7 = request.POST['fight7']
    fighter8 = request.POST['fight8']
    context = fight_setup(str.title(fighter1),str.title(fighter2),str.title(fighter3), str.title(fighter4), str.title(fighter5), str.title(fighter6), str.title(fighter7), str.title(fighter8))
    return render(request, 'whiskeywheel/wheelpage.html', context)

#signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = SignupForm()
    return render(request, 'whiskeywheel/signup.html', {'form':form})
    

#login page
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'whiskeywheel/login.html', {'form':form})


#logout page
def user_logout(request):
    logout(request)
    return redirect('login')