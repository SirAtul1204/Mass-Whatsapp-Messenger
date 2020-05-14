#Whatsapp API = "https://api.whatsapp/send?phone=91XXXXXXXXXXXX"
#https://wa.me/whatsappphonenumber/?text=
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request, urllib.parse, urllib.error
msg = '''Automated_Whatsapp_Msg_1'''
driver = webdriver.Chrome(executable_path="/mnt/e/Python/Selenium/chromedriver_win32/chromedriver.exe")

driver.get("https://web.whatsapp.com/")
#driver.find_element_by_xpath("//*[@id='sites-canvas-main-content']/table/tbody/tr/td/div/div[5]/ul/li[1]/a").click()
#driver.back()
print('Pausing')
time.sleep(15) #You have 15 seconds to login by scanning the QR Code if you need more time increase the value in sleep()
print('Resuming')
serviceurl = "https://wa.me/919406132776/?"
params = dict()
params['text'] = msg
url = serviceurl + urllib.parse.urlencode(params)
print(url)
driver.get(url)
driver.find_element_by_xpath("//*[@id='action-button']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
time.sleep(6)
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
