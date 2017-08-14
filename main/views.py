from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.safestring import mark_safe
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
            return redirect('/dashboard')
        else:
            print(errors)
            errors = {'error': '用户名或者密码错误，请重新输入'}
            return render(request, 'login.html', errors)

@login_required(login_url='/login/')
def dashboard(request):
    if request.method == 'GET':
        docker_container_all = docker_initial().docker_container_dictionary()
        # print(docker_container_all)
        return render(request, 'dashboard.html', {'docker_container_all': docker_container_all})

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

@login_required(login_url='/login/')
def logs(request):
    if request.method == 'GET':
        hostname  = request.GET.get('hostname')
        container_name = request.GET.get('container_name')
        docker_container_all = docker_initial().docker_container_dictionary()
        container_all = docker_container_all[hostname]
        for i in container_all:
            if i.name == container_name:
                b_logs = i.logs(tail=10)
        logs_str = mark_safe(str(b_logs, encoding="utf-8").replace('\n', '<br/>'))
        logs={'logs':logs_str}
        return render(request, 'logs.html', logs)
        #获取到了容器的name 然后去lib中搜索name的容器然后进行日志打印