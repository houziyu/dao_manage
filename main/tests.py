from django.test import TestCase
import datetime
import docker


docker_singleton = docker.DockerClient(base_url='tcp://47.92.136.150:2375')
aa= datetime.datetime.now() + datetime.timedelta(hours=-1)
print(aa)
bb = []
docker_list  = docker_singleton.containers.list()
for i in docker_list:
    if i.name == 'order-service-16':
        bb.append(i)
print(bb[0].logs(since=aa))