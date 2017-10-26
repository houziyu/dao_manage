from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from main.lib import docker_initial
from django.http import StreamingHttpResponse
from config import dao_config
from main import models
import os,zipfile,json,datetime
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import paramiko
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
        log_path = dao_config.log_dir_master
        service_name_all = []
        list = os.listdir(log_path)
        for line in list:
            filepath = os.path.join(log_path, line)
            if os.path.isdir(filepath):
                service_name_all.append(line)
        return render(request, 'dir_log.html', {'service_now': service_name_all})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def performance(request):
    hostmenu = request.GET.get('hostmenu')
    container = request.GET.get('container')
    docker_container_all = docker_initial().docker_container_dictionary()
    aaa = {}
    bbb = []
    for i in docker_container_all:
        for y in docker_container_all[i]:
            bbb.append(y.name)
        aaa[i] = bbb
        bbb = []
    j_str = json.dumps(aaa)
    if hostmenu and container:
        row = models.monitoring_data.objects.filter(container_name=container,name=hostmenu).order_by('-datetime')[:7]
        cpu = []
        mem = []
        time = []
        print(row)
        for i in row :
            mem.append(i.mem)
            new_time = i.datetime + datetime.timedelta(hours=8)
            # time.append(new_time.strftime('%H:%M:%S'))
            time.append(new_time.strftime("%H:%M:%S"))
            cpu.append(i.cpu)
        print(time)
        print(mem)
        print(cpu)
        host_all = {'time':time,'mem':mem,'cpu':cpu}

        print(host_all['time'])
        return render(request, 'performance.html', {'docker_container_all': docker_container_all, 'j_str': j_str,'host_all':host_all})
    else:
        print(j_str)
        return render(request, 'performance.html', {'docker_container_all':docker_container_all,'j_str':j_str})

def data_acquisition(request):
    docker_container_all = docker_initial().docker_container_dictionary()
    for i in docker_container_all:
        # 主机名称
        docker_name = i
        for y in docker_container_all[docker_name]:
            container_stats_now = y.stats(stream=False)
            # print(pprint.pformat(bb))
            # cpu使用百分比
            cpu_total_usage = container_stats_now['cpu_stats']['cpu_usage']['total_usage']
            pre_cpu_total_usage = container_stats_now['precpu_stats']['cpu_usage']['total_usage']
            system_usage = container_stats_now['cpu_stats']['system_cpu_usage']
            pre_system_usage = container_stats_now['precpu_stats']['system_cpu_usage']
            per_cpu_usage_array = container_stats_now['precpu_stats']['cpu_usage']['percpu_usage']
            cpu_delts = cpu_total_usage - pre_cpu_total_usage
            system_delta = system_usage - pre_system_usage
            CPU = ((cpu_delts / system_delta) * len(per_cpu_usage_array)) * 100
            CPU = round(CPU, 2)
            # print('cpu', CPU)  # string
            # 内存信息
            mem_usage = container_stats_now['memory_stats']['stats']['active_anon']
            mem_limit = container_stats_now['memory_stats']['limit']
            mem = round((mem_usage / mem_limit) * 100, 2)
            mem_usage_m = round(mem_usage / 1024 / 1024, 2)
            # print('mem', mem)
            # print('mem_usage_m', mem_usage_m)
            # 网络信息
            net_i = round(container_stats_now['networks']['eth0']['rx_bytes'] / 1024 / 1024, 2)
            net_o = round(container_stats_now['networks']['eth0']['tx_bytes'] / 1024 / 1024, 2)
            # print('net_i:', net_i)
            # print('net_o:', net_o)
            # 时间信息
            # read_time = container_stats_now['read'].split('.')[0]
            # gmt_time = datetime.datetime.strptime(read_time, '%Y-%m-%dT%H:%M:%S') + datetime.timedelta(hours=8)
            # print(gmt_time)  # datetime
            # 容器名称
            container_name = container_stats_now['name'].split('/')[1]
            # print(container_name)
            models.monitoring_data.objects.create(cpu=CPU, mem_usage=mem_usage_m, mem=mem, net_i=net_i, net_o=net_o,
                                                  container_name=container_name, name=docker_name)
            return_data = \
                {docker_name:
                    {container_name:
                        {
                            'cpu': CPU,
                            'mem_usage': mem_usage_m,
                            'mem': mem,
                            'net_i': net_i,
                            'net_o': net_o,
                        }
                    }
                }
            # print(return_data)
    return HttpResponse('ok')

@login_required(login_url='/login/')
def script(request):
    script_all = models.script_data.objects.all()
    return render(request, 'script.html',context={'script_all':script_all})

@login_required(login_url='/login/')
def script_execution(request):
    script_path = request.GET.get('script_path')
    server_name = request.GET.get('server_name')
    script_parameter = request.GET.get('script_parameter')
    script_status = models.script_data.objects.filter(script_path=script_path).all()[0].status
    if script_status == 1 :
        models.script_data.objects.filter(script_path=script_path).update(status=2)
        if script_parameter == '无':
            script_parameter = ''
        result = ssh_connect(server_name,script_path,script_parameter)
        result = mark_safe(result)
        models.script_data.objects.filter(script_path=script_path).update(status=1)
        return render(request, 'script_results.html', {'result':result})
    elif script_status == 2 :
        error = '正在编译。请稍后再试。'
        return render(request, 'script_results.html', {'error':error})

def ssh_connect(server_name,script_path,script_parameter):
    pkey = paramiko.RSAKey.from_private_key_file(dao_config.key_address)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command = "bash" + ' ' +script_path + ' ' + script_parameter
    print(command)
    ssh.connect(
                hostname=server_name,
                port=22,
                username='root',
                pkey=pkey)
    stdin, stdout, stderr = ssh.exec_command(command)
    # out_log_all=stdout.readlines().decode()
    out_log_all = stdout.read().decode()
    err_log_all=stderr.read().decode()
    ssh.close()
    if err_log_all:
        return err_log_all
    return   out_log_all

