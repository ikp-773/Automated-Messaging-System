from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com')
input('Press anything to start after connecting with WhatsApp web.  ')
fhandle = open('allstars.txt')  #  # You can add another text file here
data = fhandle.read()
lines = data.split('\n')
i = 0
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys('Contact Name')  # Enter the name of a contact on your phone
time.sleep(1)
name = driver.find_element_by_class_name('_2kHpK')
name.click()
time.sleep(1)
for line in lines:
    while True:
        msg = driver.find_element_by_class_name('_3uMse')
        msg.send_keys(lines[i])
        time.sleep(5)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()
        time.sleep(5)
        i = i + 1
        print(i)