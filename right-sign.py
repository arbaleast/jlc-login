import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from system_type import system

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.add_argument('--disable-gpu')
options.set_preference('permissions.default.image', 2)
print("浏览器驱动位置： ", system())
ser = Service(system())
browser = webdriver.Firefox(service=ser, options=options)

def main():
	
	browser.get('https://www.right.com.cn/FORUM/member.php?mod=logging&action=login')

	print("输入账号密码中\n")
	browser.find_element(By.CSS_SELECTOR, 'td>input[name="username"]').send_keys('agjhkjk')
	browser.find_element(By.CSS_SELECTOR, 'td>input[name="password"]').send_keys('DAUkKaCGEt4hudZ')

	browser.find_element(By.CSS_SELECTOR, 'input[name="cookietime"]').click()

	browser.find_element(By.CSS_SELECTOR, 'button[name="loginsubmit"]').click()
	print("已登录\n")

	time.sleep(10)
	browser.find_element(By.CSS_SELECTOR, 'div#um>p>a:last-child').click()
	print("已退出登录")
	time.sleep(2)
main()
browser.quit()
