# Google login module
from selenium.webdriver.support.ui import WebDriverWait
import logging
from time import sleep

def loggin_google (driver,usuario,password):
	user=driver.find_element_by_id('Email')
	user.clear()
	user.send_keys(usuario)

	next=driver.find_element_by_id('next')
	next.click()
	logging.info(usuario)

	sleep( 1 )
	wait = WebDriverWait(driver, 20)
	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds
	contrasena=driver.find_element_by_id('Passwd')

	wait = WebDriverWait(driver, 20)
	#contrasena.clear()
	contrasena.send_keys(password)

	next=driver.find_element_by_id('signIn')
	next.click()
