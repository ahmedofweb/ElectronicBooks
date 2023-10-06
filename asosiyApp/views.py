from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from .models import *

def home(request):
    return render(request, 'home.html')
def bolim(request):
    content = {
        'bolimlar': Bolim.objects.all()
    }
    return render(request, 'bolimlar.html', content)

def kitoblar(request):
    content = {
        'kitoblar': Kitob.objects.all()
    }
    return render(request, 'kitoblar.html', content)

def kitob_qoshish(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Kitob.objects.create(
                nom=request.POST.get('nom'),
                muallif=Muallif.objects.filter(ism=request.POST.get('muallif'))[0],
                yili=request.POST.get('yil'),
                bolim=Bolim.objects.filter(nom=request.POST.get('bolim'))[0],
                file=request.POST.get('file'),
                user=request.user
            )
            return redirect('/kitoblar/')
        content = {
            'mualliflar': Muallif.objects.all(),
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'kitob_qoshish.html', content)
    return redirect('/login/')


def kitoblarim(request):
    if request.user.is_authenticated:
        content = {
            'kitoblar': Kitob.objects.filter(user=request.user)
        }
        return render(request, 'kitoblarim.html', content)
    return redirect('/login/')

def kitob(request, pk):
    content = {
        'i': Kitob.objects.get(id=pk)
    }
    return render(request, 'kitob.html', content)

def kitob_tahrirlash(request, pk):
    kitob = Kitob.objects.get(id=pk)
    content = {
        'kitob': kitob
    }
    return render(request, 'kitob_tahrirlash.html', content)
def mualliflar(request):
    content = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, 'mualliflar.html', content)

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('login'),
            password=request.POST.get('parol')
        )
        if user is None:
            return redirect('/login/')
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def yangi_asarlar(request):
    content = {
        'kitoblar': Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'yangi_asarlar.html', content)
