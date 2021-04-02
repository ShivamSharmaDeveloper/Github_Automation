import sys
from selenium import webdriver
import os
import getpass

email = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

reponame = sys.argv[1]
path = os.environ.get('Ga')

browser = webdriver.Chrome()    # Paste your Chrome driver into python folder
browser.get('http://github.com/login')


browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(email)
browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
browser.get('https://github.com/'+ email + '/' + reponame + '/settings')
browser.find_elements_by_xpath('/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/summary')[0].click()
browser.find_elements_by_xpath(
        '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(email + '/' + reponame)
browser.find_elements_by_xpath(
        '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()

os.chdir(path)
os.system(f'rmdir /s {reponame}')

print('Respository is deleted')
