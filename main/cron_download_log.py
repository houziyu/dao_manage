from .lib import docker_initial
def cron_download_log():
    docker_container_all = docker_initial().docker_container_dictionary()
    for i in docker_container_all:
        hostname= i
        for y in docker_container_all[i]:
            if y.name == "job-service-8500":
                log_init = y.get_archive('/logs/job-service/info/log-info-2017-08-20.0.log')
                log_str = str(log_init[0].data, encoding="utf-8")
                print(log_str)
            # print(hostname,y.name,)
    # datetime_now = datetime.datetime.now().strftime('%Y-%m-%d')
    # os.mkdir('./log/')
    # for i in docker_container_all:
    #     hostname = i
    #     for y in docker_container_all[i]:
    #         log_name = hostname+'_'+y.name+'_'+datetime_now+'.log'
    #         os.mkdir('./log/'+y.name)
    #         logs_file = open('./log/'+y.name+'/'+log_name,'a+')
    #         log_str = str(y.logs(),encoding="utf-8")
    #         logs_file.write(log_str)
    #         logs_file.close()
if __name__ == '__main__':
    cron_download_log()