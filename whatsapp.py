from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
filepath = input('Enter your filepath(images/video) : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attechment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
attechment_box.click()
image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(filepath)

sleep(3)

send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()



