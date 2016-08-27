# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time, sys
import HTMLTestRunner
reload(sys)
import os



class Baidu(unittest.TestCase):
    """SAML SP Test"""

    def setUp(self):
        profile_dir=r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"    # 对应你的chrome的用户数据存放路径  
        chrome_options=webdriver.ChromeOptions()  
        chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
        self.driver = webdriver.Chrome(chrome_options=chrome_options)  
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.zhihu.com/"

    def test_baidu_search(self):
        driver = self.driver
        print u"========【case_0001】 fuck search long time============="
        driver.get(self.base_url + "/")
        # driver.find_element_by_id("kw").clear()
        # driver.find_element_by_id("kw").send_keys(u"林志玲")
        # driver.find_element_by_id("su").click()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = 'C:\\Workspace\\HTMLTestRunner\\result\\image\\'+now+'.png'
        print pic_path
        driver.save_screenshot(pic_path)
        time.sleep(58)
    def ddest_baidu2_search(self):
        driver = self.driver
        print u"========【case_0001】 fuck search long time============="
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kdsew").clear()
        driver.find_element_by_id("kwsdr").send_keys(u"林志玲")
        # driver.find_element_by_id("su").click()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = 'C:\\Workspace\\HTMLTestRunner\\result\\image\\'+now+'.png'
        print pic_path
        print "hello"
        driver.save_screenshot(pic_path)
        time.sleep(2)
           

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
#     testunit.addTest(Baidu("test_baidu2_search"))
    HtmlFile = "C:\\Workspace\\HTMLTestRunner\\result\\HTMLtemplate.html"
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Who knows why eclipse pass", description=u"search long time")
    runner.run(testunit)
    fp.close()
