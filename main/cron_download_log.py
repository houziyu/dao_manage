from main.lib import docker_initial
import datetime
from config import dao_config
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
                    log_local_name = '/log_everyone_bak/' + service_name + '-service/' + hostname + '-' + service_name + '-service' + '-' + log_date + '.log'
                    log_file = open(log_local_name, 'a+')
                    log_file.write('执行时间:'+log_date)
                    log_file.write(log_str)
                    log_file.close()