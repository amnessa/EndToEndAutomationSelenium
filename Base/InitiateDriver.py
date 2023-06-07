import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from Library import ConfigReader
from selenium.webdriver.chrome.options import Options

def startBrowser():
    global driver

    if((ConfigReader.readConfigData('Details','Browser'))=="chrome"):
        path="../Driver/chromedriver.exe"
        driver =Chrome(executable_path=path)
    elif((ConfigReader.readConfigData('Details','Browser'))=="firefox"):
        path = "../Driver/geckodriver.exe.exe"
        driver_service = Service(executable_path=path)
        driver = webdriver.Firefox(service=driver_service)

    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()

