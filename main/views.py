from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index_login(request):
    errors = {}
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            print('authenticate sucess')
            login(request, user)
            return render(request, 'index.html')
        else:
            errors = {'error': 'wrong username or password'}
    return render(request, 'login.html', errors)