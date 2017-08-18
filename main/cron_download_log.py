from main.lib import docker_initial
import os
import datetime
def cron_download_log():
    docker_container_all = docker_initial().docker_container_dictionary()
    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d')
    os.mkdir('./log/')
    for i in docker_container_all:
        hostname = i
        for y in docker_container_all[i]:
            log_name = hostname+'_'+y.name+'_'+datetime_now+'.log'
            os.mkdir('./log/'+y.name)
            logs_file = open('./log/'+y.name+'/'+log_name,'a+')
            log_str = str(y.logs(),encoding="utf-8")
            logs_file.write(log_str)
            logs_file.close()
