from django.test import TestCase
import datetime
import docker


docker_singleton = docker.DockerClient(base_url='tcp://docker_node2:2375')
docker_list  = docker_singleton.containers.list()
aa= docker_list[0].get_archive('/usr/local/apache2/conf')
print(type(aa[0]))
