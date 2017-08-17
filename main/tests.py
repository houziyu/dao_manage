from django.test import TestCase
import datetime
import docker
import re


aa = 'at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3909)<br/>      at com.mysql.jdbc.MysqlIO.sendCommand(MysqlIO.java:2527)<br/>     at com.mysql.jdbc.MysqlIO.sqlQueryDirect(MysqlIO.java:2680)<br/>        at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2501)<br/>   at com.mysql.jdbc.PreparedStatement.executeInternal(PreparedStatement.java:1858)<br/>   at com.mysql.jdbc.PreparedStatement.execute(PreparedStatement.java:1197)<br/>     at sun.reflect.GeneratedMethodAccessor137.invoke(Unknown Source)<br/>   at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)<br/>     at java.lang.reflect.Method.invoke(Method.java:498)<br/>        at org.apache.ibatis.logging.jdbc.PreparedStatementLogger.invoke(PreparedStatementLogger.java:59)<br/>    at com.sun.proxy.$Proxy185.execute(Unknown Source)<br/> at org.apache.ibatis.executor.statement.PreparedStatementHandler.query(PreparedStatementHandler.java:63)<br/>   at org.apache.ibatis.executor.statement.RoutingStatementHandler.query(RoutingStatementHandler.java:79)<br/>ce)<br/>'
bb = re.sub(r'at','      at',aa)
print(bb)
# docker_singleton = docker.DockerClient(base_url='tcp://47.92.136.150:2375')
# aa= datetime.datetime.now() + datetime.timedelta(hours=-1)
# print(aa)
# bb = []
# docker_list  = docker_singleton.containers.list()
# for i in docker_list:
#     if i.name == 'order-service-16':
#         bb.append(i)
# print(bb[0].logs(since=aa))
