from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time
import os
import sys
import getpass

email = input("Enter your email or username: ")
password = getpass.getpass("Enter your password: ")

foldername = str(sys.argv[1])
path = os.environ.get('Ga')           #os.path.join('C:/Users/Documents/Projects')
_dir = path + '/' + foldername

driver = webdriver.Chrome() # Paste your Chrome driver into python folder
driver.get('https://github.com/login')

user = driver.find_element_by_id('login_field')
user.send_keys(email)

user = driver.find_element_by_id('password')
user.send_keys(password)

sign = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]')
sign.submit()

time.sleep(2)

new = driver.find_element_by_xpath('/html/body/div[4]/div/aside/div[2]/div[1]/div/h2/a')
new.click()

time.sleep(4)

new = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
new.send_keys(foldername)

create = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
create.submit()

time.sleep(4)

#clone = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[3]/div/form[2]/button')
#clone.click() # Unhash this if you r using SSH 

copy = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy')
copy.click()

git_url = clipboard.paste()
print(git_url)

os.mkdir(_dir)
os.chdir(_dir)
os.system('git init')
os.system(f'echo "# {foldername}" > README.md')
os.system('git add README.md')
os.system('git commit -m "initial commit"')
os.system('git remote add origin '+ git_url)
os.system('git push -u origin master')

driver.refresh()

print(f'{foldername} created automatically')
os.system('code .')
print('\n Task Completed...')
