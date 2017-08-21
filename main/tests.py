# from django.test import TestCase
# import datetime
import docker
#
#
# docker_singleton = docker.DockerClient(base_url='tcp://docker_node2:2375')
# docker_list  = docker_singleton.containers.list()
# aa= docker_list[0].get_archive('/usr/local/apache2/conf')
#


def cron_download_log():
    docker_singleton = docker.DockerClient(base_url='tcp://docker_dev2:2375')
    docker_list = docker_singleton.containers.list()
    for i in docker_list:
        if i.name == "job-service-8500":
            log_init = i.get_archive('/logs/job-service/info/log-info-2017-08-20.0.log')
            log_str = str(log_init[0].data, encoding="utf-8")
            print(log_str)
            # print(hostname,y.name,)
    # datetime_now = datetime.datetime.now().strftime('%Y-%m-%d')
    # os.mkdir('./log/')
    # for i in docker_container_all:
    #     hostname = i
    #     for y in docker_container_all[i]:
    #         log_name = hostname+'_'+y.name+'_'+datetime_now+'.log'
    #         os.mkdir('./log/'+y.name)
    #         logs_file = open('./log/'+y.name+'/'+log_name,'a+')
    #         log_str = str(y.logs(),encoding="utf-8")
    #         logs_file.write(log_str)
    #         logs_file.close()
if __name__ == '__main__':
    cron_download_log()