from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
import docker
# Create your views here.

def index_login(request):
    errors = {}
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            print('authenticate sucess')
            login(request, user)
            return render(request, 'index.html')
        else:
            errors = {'error': '用户名或者密码错误，请重新输入'}
    return render(request, 'login.html', errors)

# @login_required()
# def index(request):
#     pass

def acc_logout(request):
    logout(request)
    return render(request, 'login.html')