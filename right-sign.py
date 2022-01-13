import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.add_argument('--disable-gpu')
options.set_preference('permissions.default.image', 2)
ser = Service("/usr/bin/geckodriver")
browser = webdriver.Firefox(service=ser, options=options)

def main():
	
	browser.get('https://www.right.com.cn/FORUM/member.php?mod=logging&action=login')

	browser.find_element(By.CSS_SELECTOR, 'td>input[name="username"]').send_keys('agjhkjk')
	browser.find_element(By.CSS_SELECTOR, 'td>input[name="password"]').send_keys('DAUkKaCGEt4hudZ')

	browser.find_element(By.CSS_SELECTOR, 'input[name="cookietime"]').click()

	browser.find_element(By.CSS_SELECTOR, 'button[name="loginsubmit"]').click()

	time.sleep(10)
	browser.find_element(By.CSS_SELECTOR, 'div#um>p>a:last-child').click()
	time.sleep(2)
main()
browser.quit()
