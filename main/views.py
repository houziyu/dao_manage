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
        # logs_str = mark_safe(str(b_logs, encoding="utf-8").replace('\n', '<br/>'))
        logs_str = mark_safe(str(b_logs, encoding="utf-8"))
        # print(str(b_logs, encoding="utf-8").replace('\n', '<br/>'))
        info={'logs':logs_str,'hostname':hostname,'container_name':container_name}
        return render(request, 'logs.html', info)
        #获取到了容器的name 然后去lib中搜索name的容器然后进行日志打印

@login_required(login_url='/login/')
def cron_download_log():
    docker_container_all = docker_initial().docker_container_dictionary()
    for i in docker_container_all:
        hostname= i
        for y in docker_container_all[i]:
            service_name = y.name.split('-')[0]
            if y.status == 'running':
                if service_name in dao_config.service_name_list:
                    aaaaa_date = str(datetime.datetime.now())
                    #时间测试
                    log_date = str(datetime.date.today() + datetime.timedelta(days=-1, hours=+8))
                    service_log_path = '/logs/' + service_name + '-service' + '/info/log-info-' + log_date + '.0.log'
                    log_init = y.get_archive(service_log_path)
                    log_str = str(log_init[0].data, encoding="utf-8")
                    log_local_name = '/log_everyone_bak/' + service_name + '-service/' + hostname + '-' + service_name + '-service' + '-' + log_date + '.log'
                    log_file = open(log_local_name, 'a+')
                    log_file.write(aaaaa_date)
                    log_file.write(log_str)
                    log_file.close()
