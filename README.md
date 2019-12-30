# MPbot  
本工具基于Python3及酷Q开发，适用于多种环境对进程进行监控。  

该工具不会再更新，有能力的自行更新扩展。

## 原理  

服务端定时运行，并监控指定进程状态，将结果写入Mysql，然后Bot得到口令，从数据库拉取最新数据。

## 运行环境  
* Pthon3  
 - 包含库  
   * psutil  
   * PyMySQL  
   
## 服务端设置  
编辑`settings.py`文件 ，按注释填写参数。  
设置定时任务执行`main.py`。  

## 酷Q插件设置  
1.在`Air\data\app`目录下新建文件夹`cn.acgnm.listener`。  
2.将`settings.json`放入该文件夹，并自行编辑该文件参数。  

## 使用方法  
在群内艾特Bot并输入ID，Bot返回该ID的最新数据。  

## 赞助  
觉得好用的请给口水喝  
![wx](https://wiki.steamsv.com/mm.png)    
