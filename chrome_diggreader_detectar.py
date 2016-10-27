#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.log_google import loggin_google
from webs.webs import landingInDiggReader
from user.user import myUser
import time
import sys
import logging

def main():
	logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
	usuario = myUser()
	
	logging.info(usuario.getDriver()) 
	driver=webdriver.Chrome(usuario.getDriver())

	if (str(sys.argv[1]) == ''):
		logging.error ('error_2: seleccionar opcion de visualizacion')
		sys.exit()
	elif (str(sys.argv[1]) == 'h'):
		driver.set_window_size(960, 1080)
	elif (str(sys.argv[1]) == 'm'):
		driver.maximize_window()
	else:
		logging.error ('error_1: seleccionar opcion de visualizacion correcta')
		sys.exit()

	#voy a Inoreader y pincho el enlace 
	landingInDiggReader(driver)

	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

	#me logueo en google.
	logging.info('%s before you %s', usuario.getUser(), usuario.getPassword())

	loggin_google (driver,usuario.getUser(),usuario.getPassword())

	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

	pinterests = driver.find_element_by_xpath('//*[@id="root-feed-list"]/li[6]')
	pinterests.click()

	pinterests = driver.find_element_by_class_name('feeditem--hdr')
	pinterests.click()

	while True:
		pinterests.send_keys("j")

		time.sleep(float(sys.argv[2]))
	
if __name__ == '__main__':
    main()





