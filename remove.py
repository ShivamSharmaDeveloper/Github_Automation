import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import getpass

email = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

reponame = sys.argv[1]
path = os.environ.get('Ga')

browser = webdriver.Chrome()    # Paste your Chrome driver into python folder
browser.get('http://github.com/login')


browser.find_elements(By.ID, 'login_field')[0].send_keys(email)
browser.find_elements(By.ID, 'password')[0].send_keys(password)
browser.find_elements(
    "xpath", '//*[@id="login"]/div[4]/form/div/input[11]')[0].click()
browser.get('https://github.com/' + email + '/' + reponame + '/settings')
browser.find_elements(
    "xpath", '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
browser.find_elements("xpath", '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[
    0].send_keys(email + '/' + reponame)
browser.find_elements(
    "xpath", '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
browser.quit()
os.chdir(path)
os.system(f'rmdir /s {reponame}')
print('Respository is deleted')
