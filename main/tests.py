# import  os
# import docker
# # import datetime
# # #
# # #
# # #
# docker_singleton = docker.DockerClient(base_url='tcp://docker_master:2375')
# docker_con = docker_singleton.containers.list()
# aa = docker_con[0]
# print(aa.stats(stream=False))
# file_name_list= {'file_name_list': {'docker_dev2-manage-service-2017-08-27.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-27.log', 'docker_dev2-manage-service-2017-08-23.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-23.log', 'docker_dev2-manage-service-2017-08-26.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-26.log', 'docker_dev2-manage-service-2017-08-22.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-22.log', 'docker_dev2-manage-service-2017-08-24.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-24.log', 'docker_dev2-manage-service-2017-08-20.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-20.log', 'docker_dev2-manage-service-2017-08-25.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-25.log'}}
#
# print(sorted(file_name_list['file_name_list'], key=str.lower))
# import  os
# def check_os_load():
#     load = os.getloadavg()
#     return (round(load[0],2),round(load[1],2),round(load[2],2))
# aa = check_os_load
# print(aa)
# for i in dd :
#     cc.append(float(i))
# print(cc)
# for i in cc:
#     print(type(i))
# aa = ['docker_dev2-manage-service-2017-08-27.log','docker_dev2-manage-service-2017-08-23.log','docker_dev2-manage-service-2017-08-26.log','docker_dev2-manage-service-2017-08-22.log','docker_dev2-manage-service-2017-08-24.log','docker_dev2-manage-service-2017-08-20.log']
# print(aa)
#
#
#
#
#
#
#
# print(sorted(aa, key=str.lower))
# print(aa.tags[-1])
# print(dir(aa))
# print(docker_con[0].image)
# print(type(docker_con[0].image))
# for i in docker_container_all:
#     hostname= i
#     for y in docker_container_all[i]:
#         service_name = y.name.split('-')[0]
#         if y.status == 'running':
#             if service_name in service_name_list:
#                 aaaaa_date = str(datetime.datetime.now())
#                 #时间测试
#                 log_date = str(datetime.date.today() + datetime.timedelta(days=-1, hours=+8))
#                 service_log_path = '/logs/' + service_name + '-service' + '/info/log-info-' + log_date + '.0.log'
#                 log_init = y.get_archive(service_log_path)
#                 print(dir(log_init))
#                 log_str = str(log_init[0].data, encoding="utf-8")
#                 log_local_name = '/log_everyone_bak/' + service_name + '-service/' + hostname + '-' + service_name + '-service' + '-' + log_date + '.log'
#                 log_file = open(log_local_name,'a+')
#                 log_file.write(aaaaa_date)
#                 log_file.write(log_str)
#                 log_file.close()
# import datetime
# service_name = 'order'
# log_date = (datetime.datetime.now() + datetime.timedelta(hours=-16)).strftime("%Y-%m-%d")
# service_log_path = '/logs/' + service_name + '-service' + '/info/log-info-' + log_date + '.0.log'
# print(service_log_path)























# docker_singleton = docker.DockerClient(base_url='tcp://docker_node2:2375')
# docker_list  = docker_singleton.containers.list()
# print(docker_list[0].status)
# print(type(docker_list[0].status))
# sdsad= 'vsiuweuuiwhviu9whv9uw9fh39r893rh893r93r939r39hr923r983rh893r893r89h389r398r'
# ss = open('dd.log','a+')
# ss.write(sdsad)
# ss.close()

# aaaaa_date = datetime.datetime.now()
# print(aaaaa_date)
# # def cron_download_log():
#     docker_singleton = docker.DockerClient(base_url='tcp://docker_dev2:2375')
#     docker_list = docker_singleton.containers.list()
#     for i in docker_list:
#         if i.name == "job-service-8500":
#             log_init = i.get_archive('/logs/job-service/info/log-info-2017-08-20.0.log')
#             log_str = str(log_init[0].data, encoding="utf-8")
#             print(log_str)
#             # print(hostname,y.name,)
#     # datetime_now = datetime.datetime.now().strftime('%Y-%m-%d')
#     # os.mkdir('./log/')
#     # for i in docker_container_all:
#     #     hostname = i
#     #     for y in docker_container_all[i]:
#     #         log_name = hostname+'_'+y.name+'_'+datetime_now+'.log'
#     #         os.mkdir('./log/'+y.name)
#     #         logs_file = open('./log/'+y.name+'/'+log_name,'a+')
#     #         log_str = str(y.logs(),encoding="utf-8")
#     #         logs_file.write(log_str)
#     #         logs_file.close()
# if __name__ == '__main__':
#     cron_download_log()

# s = 'order-service-8101'
# b = 'ordervdsevice.1.dsfajoijoi932irw0j320n'
# print(s.split('-')[0])
# print(b.split('-')[0])

# import zipfile
# file_path = '/Users/yunque/Downloads/123.zip'
# archive = zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED)
# archive.write('/Users/yunque/Downloads/order.log')
# archive.close()
