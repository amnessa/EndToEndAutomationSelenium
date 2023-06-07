from behave import *
from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def before_feature(context,feature):  #we have before_all, before_feature, before_scenario, before_tag, before_step
    path = "../Driver/chromedriver.exe"
    driver_service = Service(executable_path=path)
    context.driver = webdriver.Chrome(service=driver_service)


def after_feature(context,feature):
    context.driver.close()