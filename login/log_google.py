# Google login module
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import logging


def loggin_google(driver, usuario, password):
    user = driver.find_element_by_id('identifierId')
    user.clear()
    user.send_keys(usuario)

	#wait = WebDriverWait(driver, 20)
	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds
	contrasena=driver.find_element_by_id('Passwd')
	contrasena.send_keys(password)

    sleep(1)
    wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds
    contrasena = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

    wait = WebDriverWait(driver, 20)
    # contrasena.clear()
    contrasena.send_keys(password)

    next = driver.find_element_by_id('passwordNext')
    next.click()


def loggin_google_theoldreader(driver, usuario, password):
    user = driver.find_element_by_id("user_login")
    user.clear()
    user.send_keys(usuario)

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds
    contrasena = driver.find_element_by_id("user_password")

    contrasena.clear()
    contrasena.send_keys(password)

    next = driver.find_element_by_xpath('//input[@type="submit"]')
    next.click()
