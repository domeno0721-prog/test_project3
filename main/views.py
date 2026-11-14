from django.shortcuts import render, redirect
from .models import Wort
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()
        
    return render(request, 'main/register.html', {'form': form})



def index(request):
    worts = Wort.objects.all().order_by('lektion')
    data = {
        'worts': worts
    }
    return render(request, "main/index.html", context=data)

def wort(request):
    return render(request, 'main/wort.html')

login_required(login_url='login')
def create(request):
    return render(request, 'main/create.html')

@login_required(login_url='login')
def add_wort(request):
    if request.method == "POST":
        ru_wort = request.POST.get('ru_wort')
        d_wort = request.POST.get('d_wort')
        lektion = request.POST.get('lektion')
    
    if not Wort.objects.filter(ru_wort=ru_wort).exists():
        Wort.objects.create(ru_wort=ru_wort, d_wort=d_wort, lektion=lektion)
            
            
    return render(request, 'main/index.html' , {'worts': Wort.objects.all()})