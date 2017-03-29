#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.log_google import loggin_google
from webs.theoldreader import landingInTheoldreader
from user.user import myUser
import time
import sys
import logging


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    usuario = myUser()

    logging.info(usuario.getDriver())
    driver = webdriver.Chrome(usuario.getDriver())

    if str(sys.argv[2]) == '':
        logging.error('error_2: seleccionar opcion de visualizacion')
        driver.quit()
        sys.exit()
    elif str(sys.argv[2]) == 'h':
        driver.set_window_size(960, 1080)
    elif str(sys.argv[2]) == 'm':
        driver.maximize_window()
    else:
        logging.error('error_1: seleccionar opcion de visualizacion correcta')
        sys.exit()

    # voy a Inoreader y pincho el enlace
    landingInTheoldreader(driver)

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds

    # me logueo en google.
    logging.info('%s before you %s', usuario.getUser(), usuario.getPassword())

    loggin_google(driver, usuario.getUser(), usuario.getPassword())

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds

    panel = driver.get("https://theoldreader.com/posts/all")

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds

    articulos = panel.find_element_by_xpath('//*[@id="post*"]').click

    articulos.send_keys("j")

if __name__ == '__main__':
    main()
