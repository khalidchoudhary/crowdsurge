########################################################
#  Script Language : Selenium Python                   #
#  ScriptName : Login.py                               #
#  TestCases: Logging and verifying content of the page#
########################################################
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

#Following are optional required
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Define Variables
baseurl = "http://crowdsurge.github.io/qa-web-tests/#/"


# Create a new instance of firefox browser object		 
driver = webdriver.Firefox()

# Navigate to page
driver.get(baseurl)

# maximize_window of open 
#driver.maximize_window()

#Verifying text on the page 
text = driver.find_elements_by_link_text('Please')

#Checking username input box exits
username = driver.find_element_by_id("username")

#Clear Username TextBox if already allowed "Remember Me"
username.clear()

#Write Username in Username TextBox
username.send_keys("qa@crowdsurge.com")

#Checking Password input box exit
password = driver.find_element_by_id("password")

#Clear Password TextBox if already allowed "Remember Me"
password.clear()

#Write Password in password TextBox
password.send_keys("crowdsurge1")

#Checking for login button
submitbutton = driver.find_element_by_class_name("btn")

#Click Login button
submitbutton.click()

#Verify welcome message of new page is loaded after successful login

#welcome_message = html/body/div[1]/div/div/h1
welcome_message = driver.find_element_by_xpath("html/body/div[1]/div/div/h1")

#Verify Logout button on new page 
logout_button = driver.find_element_by_xpath("html/body/div[1]/div/div/nav/div[2]/ul/li/a")

#Verify link button on new page 
crowdsurge_link = driver.find_element_by_xpath("html/body/div[1]/div/div/nav/div[1]/a")


#Close the current window
driver.close()



