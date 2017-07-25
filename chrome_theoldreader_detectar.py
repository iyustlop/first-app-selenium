#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.log_google import loggin_google_theoldreader
from webs.theoldreader import landingInTheoldreader
from user.user import MyUser
import time
import sys
import logging


def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    usuario = MyUser()

    logging.info(usuario.driver())
    driver = webdriver.Chrome(usuario.driver())

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
    logging.info('%s before you %s', usuario.user(), usuario.password())

    loggin_google_theoldreader(driver, usuario.user(), usuario.password())

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds

    panel = driver.get("https://theoldreader.com/posts/all")

    driver.implicitly_wait(20)  # //gives an implicit wait for 20 seconds

    articulos = panel.find_element_by_xpath('//*[@id="post*"]').click

    articulos.send_keys("j")

if __name__ == '__main__':
    main()
