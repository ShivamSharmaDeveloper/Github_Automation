from selenium import webdriver
from selenium.webdriver.common.by import By
import clipboard
import time
import os
import sys
import getpass
from webdriver_manager.chrome import ChromeDriverManager

email = input("Enter your email or username: ")
password = getpass.getpass("Enter your password: ")

foldername = str(sys.argv[1])
path = os.environ.get('Ga')  # os.path.join('C:/Users/Documents/Projects')
_dir = path + '/' + foldername

# Paste your Chrome driver into python folder
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://github.com/login')

user = driver.find_element(By.ID, 'login_field')
user.send_keys(email)

user = driver.find_element(By.ID, 'password')
user.send_keys(password)

sign = driver.find_element(
    "xpath", '//*[@id="login"]/div[4]/form/div/input[11]')
sign.submit()

time.sleep(20)

new = driver.find_element(
    By.CSS_SELECTOR, ('body > div.logged-in.env-production.page-responsive.full-width > div.application-main > div > aside > div > loading-context > div > div.mb-4.Details.js-repos-container.mt-5 > div > h2 > a'))
new.click()

time.sleep(4)

new = driver.find_element("xpath", '//*[@id="repository_name"]')
new.send_keys(foldername)

create = driver.find_element(
    "xpath", '//*[@id="new_repository"]/div[5]/button')
create.submit()

time.sleep(4)

#clone = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[3]/div/form[2]/button')
# clone.click() # Unhash this if you r using SSH

copy = driver.find_element(
    "xpath", '//*[@id="repo-content-pjax-container"]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy')
copy.click()

git_url = clipboard.paste()
print(git_url)

os.mkdir(_dir)
os.chdir(_dir)
os.system('git init')
os.system(f'echo "# {foldername}" > README.md')
os.system('git add README.md')
os.system('git commit -m "initial commit"')
os.system('git remote add origin ' + git_url)
os.system('git push -u origin master')

driver.refresh()

print(f'{foldername} created automatically')
os.system('code .')
print('\n Task Completed...')
os.system('exit')
