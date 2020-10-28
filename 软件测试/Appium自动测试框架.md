#### Appium 自动化测试框架
## Appium介绍
Appium是一个移动端自动化框架 可测试原生应用 移动网页应用和混合型应用是跨平台的 可用于android和ios操作系统
## Appium python库安装
```
pip install appium-python-client
```
## 启动参数 / 前置代码
```

from appium import webdriver   
import time

desired_caps = dict()                               //创建一个空字典
desired_caps['platformName'] = 'Android'            //平台名 大小无所谓不能乱写
desired_caps['platformVersion'] = '8.1'             //平台对应的版本 小版本兼容
desired_caps['deviceName'] = '192.168.79.105:5555'  //设备名不可为空 ios不可随意便编写 android随意
desired_caps['appPackage'] = 'com.android.settings' // 需要启动的包名
desired_caps['appActivity'] = '.Settings'           //需要启动的程序名

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```
## Appium基础操作
#### 通过代码跳转到其他app
```
start_activity("包名","程序名")
```
#### 获取包名界面名
```
driver.current_package  //获取包名
driver.current_activity //获取界面名
```
#### 如何通过代码关闭app和驱动对象
* 通过driver对象调用close_app方法
    * 关闭当前应用程序 不会关闭驱动对象  
* 通过driver对象调用quit方法
    * 关闭驱动对象 同时关闭驱动对象所关联的app
#### 安装和卸载以及是否安装app
```
driver.is_app_installed()   //判断应用是否安装
```
```
driver.remove_app()         //卸载app
```
```
driver.install_app()        //安装app
```
#### 将应用置于后台(模拟热启动 自动回到前台)
```
driver.background_app(秒)   //进入后台5秒自动归位
```
#### 模拟home键位 (冷启动)
```
driver.background_app()
```
#### UIAutomatorViewer 
##### 用来扫描和分析android UI工具
```
adb shell uiautomator dump /sdcard/app.uix
adb pull /sdcard/app.uix E:/app.uix
adb shell screencap -p /sdcard/app.png
adb pull /sdcard/app.png E:/app.png
```
* 个人采用Appium自带的元素定位器

## 元素定位操作API

#### 定位一个元素
```
//通过 id定位一个元素
//id_value 元素resource_id的属性值
driver.find_element_by_id(id_value)
//通过 class定位一个元素
//id_class 元素resource_id的属性值
driver.find_element_by_class_name(class_value)
//通过 xpath定位一个元素
//xpath_value 元素xpath的表达式
driver.find_element_by_xpath(xpath_value)
```
#### 定位一组元素
```
//通过 id定位一个元素
//id_value 元素resource_id的属性值
driver.find_elements_by_id(id_value)
//通过 class定位一个元素
//id_class 元素resource_id的属性值
driver.find_elements_by_class_name(class_value)
//通过 xpath定位一个元素
//xpath_value 元素xpath的表达式
driver.find_elements_by_xpath(xpath_value)
```
#### 定位元素的注意点
* 如果使用find_element_by_xxxx 传入了一个没有的条件会报错 NoSuchElementException
* 如果find_elemet_by_xxxx传入了一个没有的条件 不会报错 返回一个空列表

## 元素等待
* 由于一些原因 我们想找的元素并没有立刻出来 此时如果直接定位可能会报错 比如以下原因
    * 由于网络速度原因
    * 由于服务器处理请求原因
    * 电脑配置原因
* WeDriver定位页面元素时如果未找到 会指定等待一段时间
#### 隐式等待
* 针对所有定位元素的超时时间为同一个值的时候
* 等待元素加载指定的时长 超出时长抛出NoSuchElementException异常
* 方式 
    * 获取driver对象后 使用driver调用implicitly_wait 方法即可

#### 显式等待
* 针对所有定位元素的超时时间设置为不同的值的时候
* 等待元素加载指定的时长 超出时长抛出TimeoutException
* 步骤
    * 导包
    * 创建 WebDriverWait 对象
    * 调用WebDriverWait 对象until方法
    * 设置了显示等待之后 可以设置一个超时时间 在这个超时时间之内进行查找 默认每0.5秒 查找一次
    * 0.5秒的频率可以设置
    * 一旦查找到元素直接操作
#### sleep
* sleep是固定死一个时间 不推荐 可能造成资源浪费
## 元素操作API
#### 点击
```
对象.click()
```
#### 输入内容
* 默认输入中文无效 但不会报错 需要在前置代码中添加代码
```
字典['unicodeKeyboard'] = True
字典['resetKeyboard'] = True

对象.send_keys(value)

```
#### 清空内容
```
对象.clear()
```
#### 获取文本框内容
```
对象.text
```