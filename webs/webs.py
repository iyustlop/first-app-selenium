import time

#landing in Inoreader and clicking the signIn

def landingInInoreader(driver):
	driver.get("http://www.inoreader.com")

	link = driver.find_element_by_id('login_air')
	NewWindow = link.click()

	googleButton = driver.find_element_by_xpath('//*[@id="landing_signin_form"]/div[3]/div[2]/button[2]')
	googleButton.click()

#landing in OldReader and clicking the signIn

def landingInOldReader(driver):
	driver.get("http://www.theoldreader.com")

	time.sleep(5)

	link = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div[1]/a[2]/i')
	NewWindow = link.click()

	#googleButton = driver.find_element_by_xpath('//*[@id="landing_signin_form"]/div[3]/div[2]/button[2]')
	#googleButton.click()

#landing in OldReader and clicking the signIn

def landingInDiggReader(driver):
	driver.get("http://www.digg.com/reader")

	#time.sleep(5)

	link = driver.find_element_by_id('step-to-sign-in')
	NewWindow = link.click()

	googleButton = driver.find_element_by_id('btn-google-auth')
	googleButton.click()
