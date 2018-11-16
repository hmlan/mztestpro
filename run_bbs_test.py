from HTMLTestRunner import HTMLTestRunner
from email.mime.text  import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
#=============定义发送邮件===================
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    #编写邮件正文,及生成的报告
    msg=MIMEText(mail_body,'html','utf-8')
    msg["Subject"]=Header("自动化测试报告",'utf-8')
    smtp=smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("username@126.com","123456")
    smtp.sendmail("username126.com","receive@126.com",msg.as_string())
    smtp.quit()
    print('email has send out!')
#=======================查找测试报告目录,找到最新生成的测试报告文件=============
def new_report(testreport):
    lists=os.listdir(testreport)
    #fn为lists列表的元素
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    """os.path.join拼接文件路径,将多个路径组合后返回,如果有一个/开头的,参数从它开始往后拼接,之前的参数全部丢弃
    ,如果有多个/开头的,从最后一个/开始往后拼接,如果有./开头的,从它上一个参数开始往后拼接"""
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new
if __name__=="__main__":
    now=time.strftime("%Y-%M-%d %H-%M-%S")
    filename='./bbs/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='魅族社区自动化测试报告',tester='may',description='环境;windows 7 浏览器:chrome')
    discover=unittest.defaultTestLoader.discover('./bbs/test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path=new_report('./bbs/report')#查找新生成的报告
    send_mail(file_path)#调用发邮件模块