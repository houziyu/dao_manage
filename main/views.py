from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from main.lib import docker_initial
from config import dao_config
import datetime
# Create your views here.

def index(request):
    return redirect('/login')

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
            print('登录完成')
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
        print(docker_container_all)
        return render(request, 'dashboard.html', {'docker_container_all': docker_container_all})

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

@login_required(login_url='/login/')
def logs(request):
    if request.method == 'GET':
        find_time=''
        hostname = request.GET.get('hostname')
        container_name = request.GET.get('container_name')
        if request.GET.get('find_time'):
            find_time = request.GET.get('find_time')
        b_logs = docker_initial().docker_logs(hostname,container_name,find_time)
        logs_str = mark_safe(str(b_logs, encoding="utf-8"))
        info={'logs':logs_str,'hostname':hostname,'container_name':container_name}
        return render(request, 'logs.html', info)
        #获取到了容器的name 然后去lib中搜索name的容器然后进行日志打印

@login_required(login_url='/login/')
def update_log(request):
    if request.method == 'GET':
        all_log = request.GET.get('all_log')
        hostname = request.GET.get('hostname')
        container_name = request.GET.get('container_name')
        if hostname and container_name:
            docker_download_log_path = docker_initial().docker_update_log(hostname,container_name)
            return render(request, 'return_index.html', docker_download_log_path)
        elif all_log:
            docker_log_bak = docker_initial().docker_update_log(all_log)
            if docker_log_bak:
                return render(request, 'return_index.html',docker_log_bak)
        else:
            errors = {'return_results':'参数传递有错误！请检查!'}
            return render(request, 'return_index.html', errors)
    return HttpResponse('aaa')

@login_required(login_url='/login/')
def download_log(request):
    pass