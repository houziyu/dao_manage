dao_manage项目
==========
1.项目的由来:
----------
>我是一名运维工程师，在新的单位接触到了新的技术。公司里面用的是`docker swarm`集群，但是在日志及监控方面真是发了愁，我试用过很多的容器管理工具`Shipyard`，但是使用起来并不那么让人满意。
启动的容器过多而且过于臃肿，我自发想自己写一个比较不错来进行管理`swarm`容器的工具。从此就诞生了`dao_manage`这个容器管理工具，`dao_manage`是一款用`python3`的`django`来进行写的，他的主要目标是1.进行日志的备份管理2.进行一个容器的监控及报警触发。
剩下的会随着新的想法来进行更新新的功能，如果有这方面需求的小伙伴，我希望你可以来联系我。共创大业！哈哈哈哈哈！<br>
-----------
2.实现方法：
-----------
>实现的方法原理，就是把`docker`中默认的本机访问改变成远程访问，在`/etc/host`文件里写好主机名对应的ip，在配置文件中`dao_config.py`跟`/etc/host`文件中`host_list`是一一对应的来进行连接，解析，调用多个`docker`接口。
现在的主要问题是每次访问后都会重新进行接口的调用，但是相对于`docker`容器存活时间及特性来讲，这种方法是成立的，但是每次调用可能会有一定的资源占用，想法是放在数据库里面但是还没想到好的方法进行解决。在日后在进行更改。
还有一点是日志的处理方式，现在日志的解决方法是根据我现公司的`docker`容器是默认写死的代码。我的初衷是写成可以自定义的。日志这方面以后需要重新思考一下解决方案。
-----------
3.测试环境示例图片：
-----------
![](https://github.com/houziyu/dao_manage/raw/master/document/img/login.png)
![](https://github.com/houziyu/dao_manage/raw/master/document/img/dashboard.png)
![](https://github.com/houziyu/dao_manage/raw/master/document/img/log.png)
![](https://github.com/houziyu/dao_manage/raw/master/document/img/oldlog.png)  
-----------
4.安装方法：
-----------
[github]:https://github.com/houziyu/dao_manage/blob/master/document/INSTALL.md "安装文档" 
-----------
5.联系方式：
-----------
>`qq及微信:469910799`