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
    def docker_logs(self,hostname,container_name,):
        datetime_now= datetime.datetime.now() + datetime.timedelta(minutes=-30)
        print(datetime_now)
        docker_container_all = docker_initial().docker_container_dictionary()
        container_all = docker_container_all[hostname]
        for i in container_all:
            if i.name == container_name:
                b_logs = i.logs(since=datetime_now) #,since=datetime.datetime.now()
                return b_logs