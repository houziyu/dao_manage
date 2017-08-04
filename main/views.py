from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from main.lib import docker_initial
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
            containers = docker_initial().docker_name()
            return render(request, 'index.html', {'containers':containers})
        else:
            print(errors)
            errors = {'error': '用户名或者密码错误，请重新输入'}
            return render(request, 'login.html', errors)

@login_required()
def index(request):
    return HttpResponse('111')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

@login_required()
def logs(request,name):
    if request.method == 'GET':
        #获取到了容器的name 然后去lib中搜索name的容器然后进行日志打印
        b_logs = docker_initial().docker_logs(name)
        logs_str = str(b_logs, encoding = "utf-8")
        logs={'logs':logs_str}
        return render(request, 'logs.html', logs)