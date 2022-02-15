import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from system_type import system

def main():
    try:
        PHNU = os.environ["PHNU"]
        NETEASE_CODE = os.environ["NETEASE_CODE"]
        #网易云自动登录
        print("###############网易云签到###############")
        print("浏览器驱动位置： ", system())
        browser.get('https://music.163.com/')
        browser.find_element(By.CSS_SELECTOR, 'div.m-tophead>a.s-fc3').click()
        #选择其他登录模式
        browser.find_element(By.CSS_SELECTOR, '.u-btn2.other').click()
        #勾选条款
        browser.find_element(By.ID, 'j-official-terms').click()

        #点击手机号登录按钮
        browser.find_element(By.CSS_SELECTOR, 'div.f-mgt10>a.u-btn2,u-btn2-2').click()
        time.sleep(0.5)
        browser.find_element(By.CSS_SELECTOR, 'div.actionbox>a.pwdlogin').click()

        #填写手机号
        browser.find_element(By.CSS_SELECTOR, 'div.txtwrap>input#p').send_keys(PHNU)
        #输入密码
        browser.find_element(By.CSS_SELECTOR, 'div.inputbox>input#pw').send_keys(NETEASE_CODE)
        #点击登录按钮
        browser.find_element(By.CSS_SELECTOR, 'div.f-mgt20>a.j-primary,u-btn2').click()


        #点击签到按钮
        time.sleep(5)
        browser.switch_to.frame('g_iframe')
        
        browser.find_element(By.CSS_SELECTOR, 'div.btnwrap>a.u-btn2').click()
        
        a = browser.find_element(By.CSS_SELECTOR, 'div.btnwrap>a.u-btn2-dis>i').text
        print(a)
        browser.quit()
    except Exception as Error:
        print(Error)

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.add_argument('--disable-gpu')
options.set_preference('permissions.default.image',2)
ser = Service(system())
browser = webdriver.Firefox(service=ser, options=options)

main()