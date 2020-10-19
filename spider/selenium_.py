# sudo pip3 install selenium
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://selenium-python.readthedocs.io/

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

input = driver.find_element_by_css_selector('#kw')
input.send_keys('炮姐图片')

button = driver.find_element_by_css_selector('#su')
button.click()