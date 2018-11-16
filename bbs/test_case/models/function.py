from selenium import webdriver
import os
import unittest
#截图函数
def insert_img(driver,file_name):
    #返回文件路径，不包含文件名
    # __file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径，为了得到绝对路径，我们需要 os.path.realpath(__file__)或者os.abspath()
    #返回当前的绝对路径(去掉最后一个路径F:/python/mztestpro/bbs/test_case)
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    #基本用法：对象.replace(rgExp,replaceText,max)
    base_dir=base_dir.replace('\\','/')
    #split()就是将一个字符串分裂成多个字符串组成的列表。并取序列为1的项
    base=base_dir.split('/test_case')[0]
    file_path=base+"/report/image/"+file_name
    #截图
    driver.get_screenshot_as_file(file_path)
if __name__=="__main__":
   driver=webdriver.Chrome()
   driver.get("http://www.baidu.com")
   insert_img(driver,'baidu.jpg')
   driver.quit()
  # # print(__file__)
   """创建截图函数,为了保持项目的移植性,采用相对路径的方式将测试截图保存到.\report\image\目录中"""
