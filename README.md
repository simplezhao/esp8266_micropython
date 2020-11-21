# MicronPython Example for ESP8266

## 开发环境

Mac + macOS Big Sur

Pycharm

### 配置

#### 安装插件

1. MicronPython

   ![image-20201121112656455](https://oss.smart-lifestyle.cn/blog/e0hk8.png)

2. Serial Port Monitor

   用于查看串口输出属于

   ![image-20201121112926991](https://oss.smart-lifestyle.cn/blog/2rut1.png)

   

   #### 工程配置

   Preferences --> Languages & Frameworks --> MicroPython

   使能MicroPython，芯片选择ESP8266，Device path根据实际串口路径配置(ls /dev/tty*)

   ![image-20201121113303750](https://oss.smart-lifestyle.cn/blog/237s6.png)

   #### 下载

   1. 单个文件下载

      右键文件，选择Run 'Flash 文件.py'

      ![image-20201121113556334](https://oss.smart-lifestyle.cn/blog/w1u9m.png)

      成功后，提示软件重启

      ![image-20201121113729262](https://oss.smart-lifestyle.cn/blog/94r74.png)

      如果提示连接失败，请检查串口是否连接，或者其他应用占用串口（使用Serial Port Monitor会占用串口，下载程序时，需要断开）

      ![image-20201121113843506](https://oss.smart-lifestyle.cn/blog/x1nyz.png)

   #### 调试&输出

   通过Serial Monitor查看print打印结果

   ![image-20201121114104188](https://oss.smart-lifestyle.cn/blog/k3xhu.png)

## 硬件

1. PyWiFI-ESP8266
2. DHT22

### PyWiFI-ESP8266 引脚图

<img src="https://oss.smart-lifestyle.cn/blog/r7z5y.png" alt="02-pyWiFi-ESP8266_引脚图 " style="zoom:67%;" />

## 软件

### REPL

