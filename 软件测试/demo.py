#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/21 13:01

from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = '192.168.79.105:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 获取driver

# print("准备进入后台")
# driver.background_app(5)
# print("已经回到前台")

# driver.start_activity("com.android.messaging", ".ui.conversationlist.ConversationListActivity")
#
# # 输出当前程序的包名和界面名
# # print(driver.current_package + "/" + driver.current_activity)
#
# time.sleep(3)
#
# driver.close_app()  # 关闭app
# print(driver.current_package + "/" + driver.current_activity)

# if driver.is_app_installed("com.tencent.android.qqdownloader"):
#     driver.remove_app("com.tencent.android.qqdownloader")
# else:
#     driver.install_app("C:\\Users\\Gei\\Downloads\\1.apk")


# # 定位id放大镜按钮
# search_button = driver.find_element_by_id("com.android.settings:id/search_action_bar")
# search_button.click()
# # 定位class输入框按钮
# driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
# # 定位xpath返回按钮
# driver.find_element_by_xpath("//*[@content-desc='Navigate up']").click(

# 定位一组元素id 返回为列表
# titles = driver.find_elements_by_id("android:id/summary")
# print(titles)
# print(len(titles))
# for title in titles:
#     print(title.text)
# print("等待结束")
# 定位一组元素class
# textview = driver.find_elements_by_class_name("android.widget.TextView")
# print(textview)
# print(len(textview))
# 查询单个未查询到会报错 查询多个元素未找到返回 空列表
# elements = driver.find_elements_by_xpath("//*[contains(@text,'a')]")
# print(len(elements))
# for element in elements:
#     print(element.text)
# time.sleep(5)

# driver.implicitly_wait(200)
# print("寻找返回")
# driver.find_element_by_xpath("//*[@content-desc='Navigate up']").click()
# print("点完了")

wait = WebDriverWait(driver, 25, 5)  # 二十五秒中内每5秒调用次 默认0.5
back_button = wait.until(lambda x: x.find_element_by_xpath("//*[@content-desc='Navigate up']"))
back_button.click()

driver.find_element_by_xpath("//*[@content-desc='Navigate up']")
time.sleep(5)



driver.quit()  # driver 直接退出
# print(driver.current_package + "/" + driver.current_activity)
