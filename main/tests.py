from django.test import TestCase
import datetime
import docker


docker_singleton = docker.DockerClient(base_url='tcp://192.168.1.147:2375')

aa= datetime.datetime.now() + datetime.timedelta(days=-1)

docker_list  = docker_singleton.containers.list()[0].logs(timestamps)
print(docker_list)



print(type(aa))
print(aa)