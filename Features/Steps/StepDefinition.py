from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'User is on Registration page')
def step_impl(context):
    path = "../Driver/chromedriver.exe"
    driver_service = Service(executable_path=path)
    context.driver = webdriver.Chrome(service=driver_service)
    context.driver.get("http://www.thetestingworld.com/testings")



@when(u'User enters username')
def step_impl(context):
    context.driver.find_element(By.NAME,'fld_username').send_keys("abcd")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element(By.NAME,'fld_email').send_keys("abcd@gmail.com")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element(By.NAME,'fld_password').send_keys("abcdqwert")


@when(u'User click on signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//input[@type="submit" and @value="Sign up"]').click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")


@when(u'User enters duplicate username')
def step_impl(context):
    print("")
