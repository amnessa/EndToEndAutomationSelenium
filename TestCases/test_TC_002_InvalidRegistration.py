
from Base import InitiateDriver
from selenium.webdriver.common.by import By
from Library import ConfigReader
from Pages import RegistrationPage

def test_InvalidRegister():

    driver=InitiateDriver.startBrowser()
    register= RegistrationPage.RegistrationClass(driver)
    register.enter_password('password')

