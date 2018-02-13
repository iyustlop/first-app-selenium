# Google login module
import logging

from selenium.webdriver.support.ui import WebDriverWait


def loggin_google(driver, usuario, password):
    user = driver.find_element_by_id('identifierId')
    user.clear()
    user.send_keys(usuario)

    next = driver.find_element_by_id('identifierNext')
    next.click()
    logging.info(usuario)

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds
    contrasena = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    contrasena.send_keys(password)

    next2 = driver.find_element_by_id('passwordNext')
    next2.click()


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
