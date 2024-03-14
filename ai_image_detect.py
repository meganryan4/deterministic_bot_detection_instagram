from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import re

def detect_ai_image_selenium(image_urls):

    xpath_text_box = "//input[@id='content-from-blog-url']"
    #xpath_button = "/html/body/div[3]/div/div[1]/div[2]/form/div[2]/button"
    xpath_button_short = "//form/div[2]/button"
    xpath_human_text = "/html/body/div[3]/div/div[1]/div[1]/div/div[1]/div[1]"
    #xpath_ai_text = "/html/body/div[3]/div/div[1]/div[1]/div/div[1]/div[2]"
    xpath_current_image = "/html/body/div[3]/div/div[1]/div[3]/img[contains(@src, '{0}')]"
    human_probability = []

    # initialize Firefox WebDriver
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    try:
        # open the website
        driver.get("https://contentatscale.ai/ai-image-detector/")

        # find the input box by its XPath (or CSS selector - driver.find_element_by_css_selector)
        input_box = driver.find_element(By.XPATH, xpath_text_box)

        # input each string from the array into the input box
        for string in image_urls:
            input_box.clear()
            # input the string
            input_box.send_keys(string)
            # possibly add a delay to simulate human interaction
            #time.sleep(1)

            # find the 'check for AI' button and click it
            button = driver.find_element(By.XPATH, xpath_button_short)
            driver.execute_script("arguments[0].click();",button)
            
            # wait until correct image is loaded in page preview
            element_present = expected_conditions .presence_of_element_located((By.XPATH, xpath_current_image.format(string)))
            WebDriverWait(driver, 10).until(element_present)

            # find the value of the human component of the image
            div = driver.find_element(By.XPATH, xpath_human_text)
            human_percent_text = div.text

            # print the extracted text
            #print(f"Percent human detected: {human_percent_text}")

            percent = [int(s) for s in re.findall(r'\b\d+\b', human_percent_text)]
            print(percent)
            p = int (percent[0])

            human_probability.append(p/100)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # close the WebDriver
        driver.quit()

    return human_probability
