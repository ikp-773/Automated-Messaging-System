from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.instagram.com')
input('Press anything to start after login. ')
fhandle = open('allstars.txt')
data = fhandle.read()
lines = data.split('\n')
i = 0
chat = driver.find_element_by_class_name('xWeGp')
chat.click()
find = driver.find_element_by_class_name('sqdOP  L3NKy   y3zKF     ')
find.click()
search = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
search.send_keys('Meghna')
name = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]')
name.click()
select = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')
select.click()
for line in lines:
    msg = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                       '2]/div/div/div[2]/textarea')
    msg.send_keys(lines[i])
    time.sleep(5)
    send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                        '2]/div/div/div[3]/button')
    # search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    # search.send_keys('')
    # time.sleep(1)
    # name = driver.find_element_by_class_name('_2kHpK')
    # name.click()
    # time.sleep(1)
    # while True:
    #     msg = driver.find_element_by_class_name('_3uMse')
    #     msg.send_keys(lines[i])
    #     time.sleep(5)
    #     button = driver.find_element_by_class_name('_1U1xa')
    #     button.click()
    i = i + 1
    print(i)
