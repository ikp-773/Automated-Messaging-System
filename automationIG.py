from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.instagram.com')
input('Press anything to start after login. ')
fhandle = open('me.txt')  # You can add another text file here
data = fhandle.read()
lines = data.split('\n')
i = 0
chat = driver.find_element_by_class_name('xWeGp')
chat.click()
time.sleep(10)
find = driver.find_element_by_class_name('QBdPU')
find.click()
time.sleep(3)
search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
search.send_keys('iabhirami')  # Enter the name of the ig account you want to send message
time.sleep(3)
name = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div')
name.click()
time.sleep(3)
select = driver.find_element_by_class_name('rIacr')
select.click()
time.sleep(3)
for line in lines:
    while True:
        msg = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                           '2]/div/div/div[2]/textarea')
        time.sleep(3)
        msg.send_keys(lines[i])
        time.sleep(5)
        send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                            '2]/div/div/div[3]/button')
        send.click()
        i = i + 1
        print(i)
