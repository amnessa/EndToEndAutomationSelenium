
import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service #for firefox we change this to from selenium.webdriver import firefox
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
import openpyxl
from DataGenerate import DataGen

@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver= InitiateDriver.startBrowser()
    register= RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_email(data[1])