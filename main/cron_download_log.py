from main.lib import docker_initial
import datetime
from config import dao_config
from urllib import request

#定时下拉备份日志 python3 manage.py crontab add  启动后记得添加上定时任务(python3 manage.py crontab remove)删除
def cron_download_log():
    docker_container_all = docker_initial().docker_container_dictionary()
    for i in docker_container_all:
        hostname= i
        for y in docker_container_all[i]:
            service_name = y.name.split('-')[0]
            if y.status == 'running':
                if service_name in dao_config.service_name_list:
                    log_date = (datetime.datetime.now() + datetime.timedelta(hours=-16)).strftime("%Y-%m-%d")
                    service_log_path = '/logs/' + service_name + '-service' + '/info/log-info-' + log_date + '.0.log'
                    log_init = y.get_archive(service_log_path)
                    log_str = str(log_init[0].data, encoding="utf-8")
                    log_local_name = dao_config.log_dir_master + service_name + '-service/' + hostname + '-' + service_name + '-service' + '-' + log_date + '.log'
                    log_file = open(log_local_name, 'a+')
                    log_file.write('执行时间:'+log_date)
                    log_file.write(log_str)
                    log_file.close()
#访问并下载容器状态数据
def download_status_data():
    response = request.urlopen(r'http://127.0.0.1:8080/data_acquisition/')  # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
    page = response.read()
    page = page.decode('utf-8')
    print(page)