from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys## 模拟键盘用的包
from selenium.webdriver.support.ui import Select##用来操作下拉列表中的选择题
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException## 找不到元素会报的错
import time##不能一直爬取页面所以需要睡一会儿
import json##用来保存网站登录cookie，以后可以免密登录网站
import os, time

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.add_argument('--disable-gpu')
ser = Service("D:\\Program Files\\geckodriver.exe")
browser = webdriver.Firefox(service=ser, options=options)

def enter_web():
	#进入登录网页
	browser.get("https://passport.szlcsc.com/login?service=https%3A%2F%2Foshwhub.com%2Flogin%3Ff%3Doshwhub")
	browser.find_element(By.XPATH, "//div[@id='normalLogin']").click()
	time.sleep(0.2)

def account_login():
	#输入账号密码登录
	browser.find_element(By.XPATH, "//input[@id='username']").send_keys("13135323109")
	time.sleep(0.2)
	browser.find_element(By.XPATH, "//input[@id='password']").send_keys("nBDd2UKq2Q1Weyh")
	time.sleep(0.2)
	browser.find_element(By.XPATH, "//div[@class='x_land2']/input").click()
	time.sleep(0.2)

def save_cookies():
	## 保存cookie
	cookies = browser.get_cookies()
	file = open('cookies.json', 'w', encoding = 'utf-8')
	json.dump(cookies, file, ensure_ascii = False)
	file.close()

def cookies_login():
	cookies = open('cookies.json', 'r', encoding = 'utf-8')
	cookie = json.load(cookies)

	for cookie in cookies:
		browser.add_cookie(cookie)

	
	browser.refresh()

def days_gift():
	days = [".three-day", ".seven-day"]

	for day in days:
		six_point = browser.find_element(By.CSS_SELECTOR, day +">img:first-child").is_displayed()
		if six_point:
			browser.find_element(By.CSS_SELECTOR, day + ">div").click()

def main():
	try:
		enter_web()
		account_login()
		save_cookies()

		#完成签到
		browser.find_element(By.CSS_SELECTOR, ".sign-header-warp>a").click()
		time.sleep(1)

		a = browser.find_element(By.CSS_SELECTOR, ".sign-action>button.btn,btn-primary").text
		print(a)

		status = browser.find_element(By.CSS_SELECTOR, '.sign-action>button.btn,btn-primary').get_attribute('disabled')
		if status != 'disabled':
			browser.find_element(By.CSS_SELECTOR, ".sign-action>button.btn,btn-primary").click()

		days_gift()

	except Exception as e:
		print(e)
	#退出浏览器
	browser.quit()

main()