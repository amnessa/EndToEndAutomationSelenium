from Library import ConfigReader
from selenium.webdriver.common.by import By
import time

class RegistrationClass:
    def __init__(self,obj):
        global driver
        driver = obj

    def enter_username(self,username):
        driver.find_element(By.NAME, ConfigReader.readElementData("Registration", "username_name")).send_keys(username)
        time.sleep(1)


    def enter_email(self, email):
        driver.find_element(By.NAME, ConfigReader.readElementData("Registration", "email_name")).send_keys(email)
        time.sleep(1)


    def enter_password(self,password):
        driver.find_element(By.NAME, ConfigReader.readElementData("Registration", "password_name")).send_keys(password)
        time.sleep(1)
