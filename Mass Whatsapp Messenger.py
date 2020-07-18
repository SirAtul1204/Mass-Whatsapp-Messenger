from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import urllib.error
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

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(10)  # Wait period for you to log-in
serviceurl = "https://web.whatsapp.com/"
params = dict()
params['text'] = msg
for contact in contact_file:
    contact = contact.rstrip()
    url = serviceurl + 'send?phone=91' + contact + '&' + \
        urllib.parse.urlencode(params) + "&source&data&app_absent"
    print(contact)
    try:
        if (contact != contact_file):
            driver.execute_script("window.onbeforeunload = function() {};")
        driver.get(url)
        time.sleep(3)

        driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div[3]/button").click()
        print("Done!")
    except:
        print("Contact not on whatsapp")
driver.quit()
