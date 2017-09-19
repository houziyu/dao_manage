# import  os
import docker,time,datetime
# from main import models
import pprint
# # import datetime
# # #
# # #
# # #
# #初始化
num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']

k = ['零', '十', '百', '千', '万', '十', '百']
import time


def rankid():
    rank = []
    for i in range(99999):
        a = tstr(i)
        rank.append(a)
    return rank


# 取整取余并连接，返回连接好的字符串和余数
def turn(x, y):
    if y >= 1:
        a = x // pow(10, y)
        b = x % pow(10, y)
        c = num[a] + k[y]
        if y > 4 and b < pow(10, 4):
            c += k[4]
        if (len(str(x)) - len(str(b))) >= 2 and b != 0:
            c += k[0]
    else:
        a = x
        b = 0
        c = num[a]

    return (c, b,)


# 调用上一个函数，以保证进行完所有的数并返回
def tstr(x):
    c = turn(x, (len(str(x)) - 1))
    a = c[0]
    b = c[1]
    while b != 0:
        a += turn(b, (len(str(b)) - 1))[0]
        b = turn(b, (len(str(b)) - 1))[1]

    return a


start = time.time()

ranki = rankid()
print(ranki)
end = time.time() - start
print('程序共用时:%0.2f' % end)
f = open('/Users/yunque/Desktop/rongNtong.txt','w+')
for i in ranki:
    name = ('荣'+i+'彤'+'\r\n')
    f.write(name)
f.close( )

# from urllib import request
# response = request.urlopen(r'http://127.0.0.1:8080/data_acquisition/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
# page = response.read()
# page = page.decode('utf-8')
# print(page)
# # def abc1():
# docker_singleton = docker.DockerClient(base_url='tcp://docker_node2:2375')
# docker_con = docker_singleton.containers.list()
# aa = docker_con[0]
# bb = aa.stats(stream=False)
# # print(pprint.pformat(bb))
# #cpu使用百分比
# cpu_total_usage = bb['cpu_stats']['cpu_usage']['total_usage']
# pre_cpu_total_usage = bb['precpu_stats']['cpu_usage']['total_usage']
# system_usage = bb['cpu_stats']['system_cpu_usage']
# pre_system_usage = bb['precpu_stats']['system_cpu_usage']
# per_cpu_usage_array = bb['precpu_stats']['cpu_usage']['percpu_usage']
# cpu_delts = cpu_total_usage - pre_cpu_total_usage
# system_delta = system_usage - pre_system_usage
# CPU = ((cpu_delts/system_delta) * len(per_cpu_usage_array)) *100
# print('cpu',CPU)  # string
# #内存信息
# mem_usage = bb['memory_stats']['stats']['active_anon']
# mem_limit = bb['memory_stats']['limit']
# mem = (mem_usage / mem_limit) *100
# print('mem',mem)
# #网络信息
# net_i = bb['networks']['eth0']['rx_bytes'] / 1024 / 1024
# net_o = bb['networks']['eth0']['tx_bytes'] / 1024 / 1024
# print('net_i:',net_i)
# print('net_o:',net_o)
# #时间信息
# read_time = bb['read'].split('.')[0]
# gmt_time = datetime.datetime.strptime(read_time, '%Y-%m-%dT%H:%M:%S') + datetime.timedelta(hours = 8)
# print(gmt_time) #datetime
# #容器名称
# container_name = bb['name']
# print(container_name.split('/')[1])
# #主机名称
# docker_name = 'docker_node2'
#
# models.monitoring_data.objects.create(cpu=CPU,mem_usage=mem_usage,mem=mem,net_i=net_i,net_o=net_o,name=docker_name)
#




# while True:
#     abc1()
#     time.sleep(2)





# print(CPU)
# print(bb)
# print(dir(aa.stats()))
# for i in aa.stats():
#     cc= str(i, encoding = "utf-8")
#     bb = eval(cc)
#     cpu_total_usage = bb['cpu_stats']['cpu_usage']['total_usage']
#     pre_cpu_total_usage = bb['precpu_stats']['cpu_usage']['total_usage']
#     system_usage = bb['cpu_stats']['system_cpu_usage']
#     print(pprint.pformat(bb))
#     pre_system_usage = bb['precpu_stats']['system_cpu_usage']
    # per_cpu_usage_array = bb['precpu_stats']['cpu_usage']['percpu_usage']
    # cpu_delts = cpu_total_usage - pre_cpu_total_usage
    # system_delta = system_usage - pre_system_usage
    # CPU = ((cpu_delts / system_delta) * len(per_cpu_usage_array)) * 100
    # print(CPU)
# print(pprint.pformat(bb))


# cc = {"read":"2017-08-29T19:01:34.206787621Z","preread":"2017-08-29T19:01:33.206874861Z","pids_stats":{"current":82},"blkio_stats":{"io_service_bytes_recursive":[{"major":8,"minor":0,"op":"Read","value":4947968},{"major":8,"minor":0,"op":"Write","value":0},{"major":8,"minor":0,"op":"Sync","value":0},{"major":8,"minor":0,"op":"Async","value":4947968},{"major":8,"minor":0,"op":"Total","value":4947968},{"major":253,"minor":0,"op":"Read","value":4947968},{"major":253,"minor":0,"op":"Write","value":0},{"major":253,"minor":0,"op":"Sync","value":0},{"major":253,"minor":0,"op":"Async","value":4947968},{"major":253,"minor":0,"op":"Total","value":4947968}],"io_serviced_recursive":[{"major":8,"minor":0,"op":"Read","value":89},{"major":8,"minor":0,"op":"Write","value":0},{"major":8,"minor":0,"op":"Sync","value":0},{"major":8,"minor":0,"op":"Async","value":89},{"major":8,"minor":0,"op":"Total","value":89},{"major":253,"minor":0,"op":"Read","value":89},{"major":253,"minor":0,"op":"Write","value":0},{"major":253,"minor":0,"op":"Sync","value":0},{"major":253,"minor":0,"op":"Async","value":89},{"major":253,"minor":0,"op":"Total","value":89}],"io_queue_recursive":[],"io_service_time_recursive":[],"io_wait_time_recursive":[],"io_merged_recursive":[],"io_time_recursive":[],"sectors_recursive":[]},"num_procs":0,"storage_stats":{},"cpu_stats":{"cpu_usage":{"total_usage":59455086046,"percpu_usage":[59455086046],"usage_in_kernelmode":1650000000,"usage_in_usermode":1220000000},"system_cpu_usage":104796220000000,"online_cpus":1,"throttling_data":{"periods":0,"throttled_periods":0,"throttled_time":0}},"precpu_stats":{"cpu_usage":{"total_usage":59454352872,"percpu_usage":[59454352872],"usage_in_kernelmode":1650000000,"usage_in_usermode":1220000000},"system_cpu_usage":104795250000000,"online_cpus":1,"throttling_data":{"periods":0,"throttled_periods":0,"throttled_time":0}},"memory_stats":{"usage":13209600,"max_usage":13447168,"stats":{"active_anon":2641920,"active_file":1564672,"cache":4681728,"hierarchical_memory_limit":9223372036854771712,"hierarchical_memsw_limit":9223372036854771712,"inactive_anon":6160384,"inactive_file":2842624,"mapped_file":2134016,"pgfault":3350,"pgmajfault":20,"pgpgin":2195,"pgpgout":503,"rss":8527872,"rss_huge":6291456,"swap":0,"total_active_anon":2641920,"total_active_file":1564672,"total_cache":4681728,"total_inactive_anon":6160384,"total_inactive_file":2842624,"total_mapped_file":2134016,"total_pgfault":3350,"total_pgmajfault":20,"total_pgpgin":2195,"total_pgpgout":503,"total_rss":8527872,"total_rss_huge":6291456,"total_swap":0,"total_unevictable":0,"unevictable":0},"limit":1912061952},"name":"/reverent_banach","id":"6dd70a08a0b84054f30897d7b2e24e37e002625c520b40352ae528b35100a268","networks":{"eth0":{"rx_bytes":1296,"rx_packets":16,"rx_errors":0,"rx_dropped":0,"tx_bytes":0,"tx_packets":0,"tx_errors":0,"tx_dropped":0}}}


# print(aa.stats().send('cpus',flags=3))
# for i in aa.stats()
#     print(i)
# a =  aa.stats().send(8)
# # for i in aa.stats():
#     print(i.next())206256957561
# file_name_list= {'file_name_list': {'docker_dev2-manage-service-2017-08-27.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-27.log', 'docker_dev2-manage-service-2017-08-23.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-23.log', 'docker_dev2-manage-service-2017-08-26.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-26.log', 'docker_dev2-manage-service-2017-08-22.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-22.log', 'docker_dev2-manage-service-2017-08-24.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-24.log', 'docker_dev2-manage-service-2017-08-20.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-20.log', 'docker_dev2-manage-service-2017-08-25.log': '/log_everyone_bak/manage-service/docker_dev2-manage-service-2017-08-25.log'}}# print(pprint.pformat(bb))
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
#
#     print(type(i))
# aa = ['docker_dev2-manage-service-2017-08-27.log','docker_dev2-manage-service-2017-08-23.log','docker_dev2-manage-service-2017-08-26.log','docker_dev2-manage-service-2017-08-22.log','docker_dev2-manage-service-2017-08-24.log','docker_dev2-manage-service-2017-08-20.log']
# print(aa)
# import itchat
# itchat.login()
# #爬取自己好友相关信息， 返回一个json文件
# friends = itchat.get_friends(update=True)[0:]
# import re
# siglist = []
# for i in friends:
#     signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
#     rep = re.compile("1f\d+\w*|[<>/=]")
#     signature = rep.sub("", signature)
#     siglist.append(signature)
# text = "".join(siglist)
#
# import jieba
# wordlist = jieba.cut(text, cut_all=True)
# word_space_split = " ".join(wordlist)
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import numpy as np
# import PIL.Image as Image
#
# coloring = np.array(Image.open("/Users/yunque/Desktop/wechat.jpg"))
# my_wordcloud = WordCloud(background_color="white", max_words=2000,
#                          mask=coloring, max_font_size=60, random_state=42, scale=2,
#                          font_path="/Users/yunque/Downloads/simhei.ttf").generate(word_space_split)
#
# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
# #
# #
# a = 1
# b = 1
# c = 0
# d = 3
# e = 3
# if e==1:
#     print('e:',e)
# elif a == 1 and b == 1 and c == 0 and d == 0 :
#     print('ok')
# elif a == 0 and b == 0 and c == 1 and d == 1 :
#     print('ok')
# else:
#     print('error')
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
