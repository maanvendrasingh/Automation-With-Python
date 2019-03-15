from selenium import webdriver
from time import sleep
import urllib.request 

base="https://www.instagram.com/"
username=input("Enter username: ")

link= base+username

browser = webdriver.Chrome()
browser.get(link)
elem=browser.find_element_by_class_name('be6sR')
img_url=elem.get_attribute('src')
print(img_url)
file=urllib.request.urlretrieve(img_url,"profile.jpg")
sleep(5)
browser.close()
