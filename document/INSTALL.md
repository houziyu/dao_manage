安装使用方法
==========
1.安装python3:
----------
>略
-----------
2.打开docker访问:
----------
>centos7的打开方法 ubuntu 应该不一样自行百度<br>
vim /lib/systemd/system/docker.service <br>
ExecStart=/usr/bin/dockerd -H 0.0.0.0:2375 -H unix:///var/run/docker.sock<br>
systemctl daemon-reload<br>
systemctl restart docker<br>
-----------
3.更改config及/etc/hosts文件：
-----------
>比如你有一台docker的ip为192.168.1.1 你想给这个docker的主机名取docker_master<br>
那你要在/etc/hosts中添加一条192.168.1.1   docker_master<br>
然后修改config中文件dao_config.py中host_list变量把 刚刚改/etc/hosts的主机名放进去<br>
修改config中文件dao_config.py中的service_name_list变量把需要查看log日志的name放进去。
-----------
4.执行shell安装脚本:
-----------
>sh document/INSTALL.sh
-----------
5.启动程序:
-----------
>python3.6 manage.py runserver 0.0.0.0:8080 --insecure<br>
或者把dao_manage中的settings.py的debug改为True之后启动<br>
python3.6 manage.py runserver 0.0.0.0:8080