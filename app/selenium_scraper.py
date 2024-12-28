# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def scrape_trending_topics():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--proxy-server=http://username:password@proxy-ip:port")
#     service = Service("D:\\Stir\\chromedriver-win64\\chromedriver.exe")  # Update with your ChromeDriver path
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         driver.get("https://x.com/i/flow/login")
#         time.sleep(5)

#         # Log in (adjust selectors if necessary)
#         username = driver.find_element(By.NAME, "text")
#         username.send_keys("ARUNSINGH435692")
#         username.send_keys(Keys.RETURN)
#         time.sleep(2)

#         password = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "password"))
#         )
#         password.send_keys("Arun@2004")
#         password.send_keys(Keys.RETURN)
#         time.sleep(5)

#         # Scrape "What's Happening" section
#         trends_section = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//section[@aria-labelledby='accessible-list-2']"))
#         )
#         trends = trends_section.find_elements(By.XPATH, ".//span[contains(text(), '#') or string-length() > 3]")
#         top_trends = [trend.text for trend in trends[:5]]

#         # Replace with an actual IP-fetching mechanism
#         ip_address = "123.45.67.89"  

#         return top_trends, ip_address

#     finally:
#         driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Add this import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

def scrape_trending_topics():
    chrome_options = Options()
#     chrome_options.add_argument("--headless")
    service = Service("D:\\Stir\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://twitter.com/login")
        time.sleep(5)

        # Update selectors here
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))
        )
        username_field.send_keys("ARUNSINGH435692")
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys("Arun@2004")
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Navigate and scrape trends
        trends_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-adyw6z r-135wba7 r-1vr29t4 r-1kihuf0') and contains(text(), 'What's happening')]"))
        )
        trends = trends_section.find_elements(By.XPATH, ".//span[contains(text(), '#') or string-length() > 3]")
        top_trends = [trend.text for trend in trends[:5]]

        # Replace with a dynamic IP fetching mechanism
        ip_address = "123.45.67.89"

        return top_trends, ip_address

    except Exception as e:
        print(f"Error in Selenium script: {e}")
        raise e

    finally:
        driver.quit()
