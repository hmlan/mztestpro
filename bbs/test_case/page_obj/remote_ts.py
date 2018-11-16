# from selenium.webdriver import Remote
# #定义主机与浏览器
# lists={'http://127.0.0.1:4444/wd/hub':'chrome','http://127.0.0.1:5555/wd/hub':'firefox'}
# #通过不同的浏览器执行脚本
# for host,browser in lists.items():
#     print(host,browser)
#     driver=Remote(command_executor=host,desired_capabilities={'platform':'ANY','browserName':browser,'version':'','javascriptEnabled':True})
#     driver.get("http://baidu.com")
#     driver.find_element_by_id("kw").send_keys(browser)
#     driver.find_element_by_id("su").click
#     driver.close()
from selenium import webdriver
d=webdriver.Edge()