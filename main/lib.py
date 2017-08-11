import docker
class docker_initial(object):
    def __init__(self):
        self.client = docker.DockerClient(base_url='tcp://192.168.1.183:2375')
    def docker_name(self):
        container_list = self.client.containers.list(all=True)
        return  container_list
    def docker_logs(self,container_name):
        logs_container = self.client.containers.list(filters={'name':container_name})[0]
        print('logs_container:',logs_container)
        print('logs_container:',logs_container.image)
        return logs_container.logs()