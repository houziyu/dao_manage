from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from main.lib import docker_initial
from django.http import StreamingHttpResponse
from config import dao_config
import os,zipfile
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
                return render(request, 'return_index.html',docker_log_bak)
        else:
            errors = {'return_results':'参数传递有错误！请检查!','log_name':None}
            return render(request, 'return_index.html', errors)
    return HttpResponse('出错了~')

@login_required(login_url='/login/')
def download_log(request):
    if request.method == 'GET':
        log_path = request.GET.get('log_path')
        log_name = request.GET.get('log_name')
        print('log_path:',log_path,'log_name:',log_name)
        #定义zip文件名称。
        zip_file_name = log_name + '.zip'
        #打包文件后置放的目录地址。
        zip_dir = dao_config.log_dir_master + 'tmp/'+ zip_file_name
        archive = zipfile.ZipFile(zip_dir, 'w', zipfile.ZIP_DEFLATED)
        #写入zip中文件的地址及名称
        archive.write(log_path)
        #写入结束
        archive.close()
        print(zip_dir)
        if os.path.isfile(zip_dir):
            response = StreamingHttpResponse(readFile(zip_dir))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(zip_file_name)
            return response
        else:
            return HttpResponse('没有这个文件') 

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
        log_path = dao_config.log_dir_master
        for i in service_name_list:
            service_name_path = log_path + i + '-service'
            service_name_service = i + '-service'
            service_name_all.append(service_name_service)
            service_now_list.append(service_name_path)
        service_now = {'service_now': service_name_all}
        return render(request, 'dir_log.html', service_now)

def html_page(request):
    service_name  = request.GET.get('service_name')
    log_path = dao_config.log_dir_master
    service_name_path = log_path + service_name
    all_file = []
    for i in os.listdir(service_name_path):
        file_path = service_name_path +'/' + i
        if os.path.isfile(file_path):
            all_file.append([i,file_path])
    print(all_file)
    all_file = sorted(all_file, key=lambda file_name: file_name[1])
    paginator = Paginator(all_file, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'cat_down_log.html', {"contacts": contacts,'service_name':[service_name]})
