import docker
from config import dao_config
import datetime

class docker_initial(object):
    def __init__(self):
        host_list = dao_config.host_list
        self.docker_all = {}
        for i in host_list:
            self.docker_singleton = docker.DockerClient(base_url='tcp://%s:2375'%i)
            self.docker_all[i] = self.docker_singleton
        print('docker_host_dictionary:',self.docker_all)

    def docker_container_dictionary(self):
        docker_container_all = {}
        for i,v in self.docker_all.items():
            docker_container_all[i]= v.containers.list(all=True)
        print('docker_container_all:',docker_container_all)
        return docker_container_all

    def docker_logs(self,hostname,container_name,find_time):
        docker_container_all = docker_initial().docker_container_dictionary()
        container_all = docker_container_all[hostname]
        if find_time:
            find_time = int(find_time)
            datetime_now= datetime.datetime.now() + datetime.timedelta(minutes=-find_time)
            print(datetime_now)
            for i in container_all:
                if i.name == container_name:
                    b_logs = i.logs(since=datetime_now) #,since=datetime.datetime.now()
                    return b_logs
        else:
            for i in container_all:
                if i.name == container_name:
                    b_logs = i.logs(tail=dao_config.log_tail_line) #,since=datetime.datetime.now()
                    return b_logs

    def docker_update_log(self,all_log=None,hostname=None,container_name=None):
        if all_log:
            print('这里是全员备份')
            docker_container_all = docker_initial().docker_container_dictionary()
            for i in docker_container_all:
                hostname = i
                for y in docker_container_all[i]:
                    service_name = y.name.split('-')[0]
                    if y.status == 'running':
                        if service_name in dao_config.service_name_list:
                            log_date = (datetime.datetime.now() + datetime.timedelta(hours=+8)).strftime("%Y-%m-%d")
                            service_log_path = '/logs/' + service_name + '-service/log_info.log'
                            log_init = y.get_archive(service_log_path)
                            log_str = str(log_init[0].data, encoding="utf-8")
                            log_dir_master = dao_config.log_dir_master
                            log_local_name = log_dir_master + service_name + '-service/update/'+'update'+ hostname + '-' + service_name + '-service' + '-' + log_date + '.log'
                            log_file = open(log_local_name, 'a+')
                            date_now = str(datetime.datetime.now())
                            log_file.write('执行时间:' + date_now)
                            log_file.write(log_str)
                            log_file.close()
            return_results = {'return_results': '!备份成功!返回主页!', 'log_name': None}
            return return_results
        elif hostname and container_name:
            print('别跑错地方了')
            docker_container_all = docker_initial().docker_container_dictionary()
            docker_container_list = docker_container_all[hostname]
            print(docker_container_list)
            for i in docker_container_list:
                if i.name == container_name:
                    service_name = i.name.split('-')[0]
                    if i.status == 'running':
                        if service_name in dao_config.service_name_list:
                            log_date = (datetime.datetime.now() + datetime.timedelta(hours=+8)).strftime("%Y-%m-%d-%H:%M:%S")
                            service_log_path = '/logs/' + service_name + '-service/log_info.log'
                            print(service_name,log_date,service_log_path)
                            log_init = i.get_archive(service_log_path)
                            log_str = str(log_init[0].data, encoding="utf-8")
                            log_name = hostname + '-' +service_name +'-'+ log_date + '.log'
                            log_dir_master = dao_config.log_dir_master
                            log_local_name = log_dir_master +'tmp/' + log_name
                            print(log_local_name)
                            log_file = open(log_local_name, 'a+')
                            date_now = str(datetime.datetime.now())
                            log_file.write('执行时间:' + date_now)
                            log_file.write(log_str)
                            log_file.close()
                            return_results = {'return_results': log_local_name,'log_name':log_name}
                            return return_results
                    else:
                        return_results = {'return_results': None, 'log_name': 'docker容器状态为exit，请检查！'}
                        return return_results