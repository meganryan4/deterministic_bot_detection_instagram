from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import re

def get_profile_details_selenium(creds):
    """ Gets the sccount's profile details using Selenium
	
	Args:
		creds: the account credentials entered

	Returns:
		array: the array of profile details: 
                has a profile picture Boolean, is followed Boolean, and follow ratio float

	"""

    # set default values
    has_profile_pic, followed, follow_ratio = False, False, 0

    xpath_popup_decline = "//button[contains(text(), 'Decline')]"
    xpath_username = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[1]/div[1]/h2"#//a[contains(@tabindex, '0')]/h2"
    xpath_has_profile_pic = "//button[contains(@title, 'profile photo')]/img[contains(@src, 'scontent')]"
    xpath_followers_cnt = "//a[contains(@href, 'followers')]/span/span"
    xpath_following_cnt = "//a[contains(@href, 'following')]/span/span"

    # initialize Firefox WebDriver
    options = webdriver.FirefoxOptions()
    #options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10) # new webdriver wait created, timeout after 10 seconds

    try:
        # open the website
        url = "https://www.instagram.com/" + creds['ig_username'] + '/'
        driver.get(url)

        # WebDriverWait(driver, 10000)
        # element = wait.until(ExpectedConditions.elementToBeClickable(By.id(“elementId”)));textToBePresentInElementLocated
        
        # wait until the permissions pop up has loaded
        element_present = expected_conditions.presence_of_element_located((By.XPATH, xpath_popup_decline))
        wait.until(element_present) # timeout is 10 secs
        popup_decline = driver.find_element(By.XPATH, xpath_popup_decline)
        popup_decline.click()

        # wait until the username has loaded
        element_present = expected_conditions.presence_of_element_located((By.XPATH, xpath_username))
        wait.until(element_present) # timeout is 10 secs

        has_profile_pic = True
        # Find elements matching the XPath expression
        #try catch
        has_profile_pic = driver.find_element(By.XPATH, xpath_has_profile_pic)

        followers = driver.find_element(By.XPATH, xpath_followers_cnt).text
        following = driver.find_element(By.XPATH, xpath_following_cnt).text

        if (followers == 0):
            followed = True

        # this prevents a divide by zero scenario
        if following == 0:
            following = 1e5
        
        
        follow_ratio = followers / following

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # close the WebDriver
        driver.quit()

    return has_profile_pic, followed, follow_ratio
