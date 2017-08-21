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