from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Load chrome driver .exe
driver = webdriver.Chrome('./chromedriver.exe')

# Generate username/password
username = 'usernameasdflkjasdf'
password = 'Hunter2'

# Open registration URL
url = 'https://mail.protonmail.com/create/new?language=enp'
driver.get(url)
time.sleep(5)

# Interact with top level elements
ps = driver.find_element_by_id('password')
psc = driver.find_element_by_id('passwordc')
ps.clear()
psc.clear()
ps.send_keys(password)
psc.send_keys(password)

# Enter iframe 1
userFrame = driver.find_element_by_xpath('//iframe[@title="Registration form" and @class="top"]')
driver.switch_to_frame(userFrame)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)

# Exit iframe 1
driver.switch_to.default_content()

# Enter iframe 2
buttonFrame = driver.find_element_by_xpath('//iframe[@title="Registration form" and @class="bottom"]')
driver.switch_to_frame(buttonFrame)
driver.find_element_by_xpath('/html/body/div/div/footer/button').click()

# Exit iframe 2
driver.switch_to.default_content()

# Confirm
time.sleep(5)
driver.find_element_by_id('confirmModalBtn').click()
time.sleep(5)

driver.quit()
