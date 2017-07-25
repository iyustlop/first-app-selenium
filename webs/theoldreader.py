from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# landing in Inoreader and clicking the signIn

button = "/html/body/div[2]/div/div/div/div/div/a[2]"

def landingInTheoldreader(driver):
    driver.get("http://www.theoldreader.com")

    wait = WebDriverWait(driver, 10)

    user = wait.until(EC.visibility_of_element_located((By.XPATH, button)))

    link = driver.find_element_by_xpath(button)
    newwindow = link.click()

