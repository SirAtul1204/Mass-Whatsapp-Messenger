# -- Made By SirAtul --
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request, urllib.parse, urllib.error
import time

msg_file = open("Message.txt")
msg = msg_file.read()
print(msg)

contact_file = None
while(contact_file is None):
    try:
        contact_file_Name = input("Enter .CSV file with name extension: ")
        contact_file = open(contact_file_Name)
    except:
        print("File not found!\nTry Again")

driver = webdriver.Chrome(executable_path = "/mnt/e/Python/Selenium/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10) #Wait period for you to log-in
serviceurl = "https://wa.me"
params = dict()
params['text'] = msg
for contact in contact_file:
    contact = contact.rstrip()
    url = serviceurl + '/' + '91' + contact + '/?' + urllib.parse.urlencode(params)
    print(contact)
    try :
        if (contact != contact_file):
            driver.execute_script("window.onbeforeunload = function() {};")
        driver.get(url)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='action-button']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
        print("Done!")
    except:
        print("Contact not on whatsapp")
driver.quit()

# -- Made by SirAtul --
