# ambari2.6集成flink1.9.1

## 一、安装包准备

ambari-flink-service-master.zip  （下载本项目）

flink-1.9.1-bin-scala_2.11.tgz  （官方的安装包）



**在ambari-server节点执行**

```shell
#删除目录
rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.6/services/FLINK
#新建目录
mkdir -p /var/lib/ambari-server/resources/stacks/HDP/2.6/services/FLINK
#解压zip包
unzip -d /var/lib/ambari-server/resources/stacks/HDP/2.6/services/FLINK ambari-flink-service-master.zip
#拷贝安装包
cp flink-1.9.1-bin-scala_2.11.tgz /var/lib/ambari-server/resources/stacks/HDP/2.6/services/FLINK/package/files/
#重启ambari server
ambari-server restart
```



## 二、ambari界面配置



![1577255064528](https://github.com/lijufeng2016/ambari-flink-service-master/blob/master/images/1577255064528.png)

![1577255143730](https://github.com/lijufeng2016/ambari-flink-service-master/blob/master/images/1577255143730.png)



勾选所有计算节点，也是就**nodemanager**节点

![1577256212350](https://github.com/lijufeng2016/ambari-flink-service-master/blob/master/images/1577256212350.png)

![1577255524109](https://github.com/lijufeng2016/ambari-flink-service-master/blob/master/images/1577255524109.png)



![1577255554417](https://github.com/lijufeng2016/ambari-flink-service-master/blob/master/images/1577255554417.png)

一路next，直到安装完成