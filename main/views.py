from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from main.lib import docker_initial
from django.http import StreamingHttpResponse
from config import dao_config
import os
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
            docker_download_log_path = docker_initial().docker_update_log(hostname=hostname,container_name=container_name)
            return render(request, 'return_index.html', docker_download_log_path)
        elif all_log:
            docker_log_bak = docker_initial().docker_update_log(all_log=all_log)
            if docker_log_bak:
                return render(request, 'return_index_all.html',docker_log_bak)
        else:
            errors = {'return_results':'参数传递有错误！请检查!'}
            return render(request, 'return_index.html', errors)
    return HttpResponse('出错了~')

@login_required(login_url='/login/')
def download_log(request):
    if request.method == 'GET':
        log_path = request.GET.get('log_path')
        log_name = request.GET.get('log_name')
        print('log_path:',log_path,'log_name:',log_name)
        the_file_name = log_name  # 显示在123弹出对话框中的默认的下载文件名
        filename = log_path  # 要下载的文件路径
        response = StreamingHttpResponse(readFile(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
        return response

def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break

@login_required(login_url='/login/')
def dir_log(request):
    if request.method == 'GET':
        service_name_list = dao_config.service_name_list
        service_now_list = []
        service_name_all = []
        file_dir = []
        file_name = []
        log_path = dao_config.log_dir_master
        for i in service_name_list:
            service_name_path = log_path + i + '-service'
            service_name_service = i + '-service'
            service_name_all.append(service_name_service)
            service_now_list.append(service_name_path)
        log_path = request.GET.get('find_name')
        if log_path:
            for i in service_now_list:
                if log_path in i:
                    print(log_path,i)
                    for y in os.listdir(i):
                        file_name.append(y)
                        filename = i+'/'+ y
                        if os.path.isfile(filename):
                            file_dir.append(filename)
                    service_now = {'service_now': file_name ,'file_dir':file_dir}
                    print(service_now)
                    return render(request, 'dir_log.html', service_now)
        else:
            service_now = {'service_now':service_name_all}
            return render(request, 'dir_log.html', service_now)