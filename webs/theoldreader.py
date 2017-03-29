#landing in Inoreader and clicking the signIn

def landingInTheoldreader(driver):
	driver.get("http://www.theoldreader.com")

	link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div/a[2]/i')
	NewWindow = link.click()

#   No es necesario, va directo a la pagina de google
#	googleButton = driver.find_element_by_xpath('//*[@id="landing_signin_form"]/div[3]/div[2]/button[2]')
#	googleButton.click()
