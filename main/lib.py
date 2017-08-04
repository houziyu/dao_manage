import docker
class docker_initial(object):
    def __init__(self):
        self.client = docker.DockerClient(base_url='tcp://192.168.1.183:2375')
    def docker_name(self):
        names = []
        container_list = self.client.containers.list()
        for i in container_list:
            names.append(i.name)
        return  names
    def docker_logs(self,container_name):
        logs_container = self.client.containers.list(filters={'name':container_name})[0]
        print('logs_container:',logs_container)
        return logs_container.logs()