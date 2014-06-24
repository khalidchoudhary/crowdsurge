######################################
# Script Language : Selenium Python  #
#  ScriptName : InvalidLogin.py      #  
#  TestCases: Invalid Logins         #
######################################
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

#Following are optional required
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

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
username.send_keys("abc@yahoo.com")

#Checking Password input box exit
password = driver.find_element_by_id("password")

#Clear Password TextBox if already allowed "Remember Me"
password.clear()

#Write Password in password TextBox
password.send_keys("Testing1")

#Checking for login button
submitbutton = driver.find_element_by_class_name("btn")

#Click Login button
submitbutton.click()

#Checking for the error message

alert = driver.switch_to_alert()

#Close the current window
driver.close()


# TestCase for checking message to enter the email address

# Create a new instance of firefox browser object		 
driver = webdriver.Firefox()

# Navigate to page
driver.get(baseurl)

#Checking username input box exits
username = driver.find_element_by_id("username")
#Clear Username TextBox if already allowed "Remember Me"
username.clear()
#Write Username in Username TextBox
username.send_keys("abc")

#Checking username input box exits
password = driver.find_element_by_id("password")
#Clear Password TextBox if already allowed "Remember Me"
password.clear()
#Write Password in password TextBox
password.send_keys("Testing1")

#Checking for login button
submitbutton = driver.find_element_by_class_name("btn")
#Click Login button
submitbutton.click()

#Checking for the error message "Please enter an email address"

alert = driver.switch_to_alert()


